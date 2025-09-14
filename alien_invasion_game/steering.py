#!/usr/bin/env python3
"""
Minimal steering-behaviours sandbox built "na mão" (from scratch) with pygame,
without using pygame.math.Vector2. Includes:
- Custom Vec2 class (ops, normalization, clamp, rotate, etc.)
- Semi-implicit Euler integrator (dt-based, framerate independent)
- Agent with steering via weighted sum
- Behaviours: seek, flee, arrive, wander, pursue
- World bounds (wrap or bounce)
- Simple debug draw and hotkeys

Controls
========
- 1: Seek mouse
- 2: Flee mouse
- 3: Arrive at mouse
- 4: Wander
- 5: Pursue a moving target (second agent)
- W: Toggle world wrap (vs bounce)
- D: Toggle debug overlays
- +/-: Adjust wander jitter
- Arrows Left/Right: Adjust arrive slowing radius
- Space: Pause/Resume simulation
- Esc or Q: Quit

Dependencies: pygame (pip install pygame)
Run: python steering_behaviors_from_scratch.py
"""
from __future__ import annotations
import math
import random
import sys
from dataclasses import dataclass
from typing import Callable, Dict, Tuple

import pygame

# ---------------------------
#  Math primitives (na mão)
# ---------------------------
class Vec2:
    __slots__ = ("x", "y")

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)

    # Representation
    def __repr__(self) -> str:
        return f"Vec2({self.x:.3f}, {self.y:.3f})"

    # Basic ops
    def __add__(self, other: "Vec2") -> "Vec2":
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vec2") -> "Vec2":
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, k: float) -> "Vec2":
        return Vec2(self.x * k, self.y * k)

    __rmul__ = __mul__

    def __truediv__(self, k: float) -> "Vec2":
        return Vec2(self.x / k, self.y / k)

    def __neg__(self) -> "Vec2":
        return Vec2(-self.x, -self.y)

    # Length / distance
    def length(self) -> float:
        return math.hypot(self.x, self.y)

    def length_sq(self) -> float:
        return self.x * self.x + self.y * self.y

    def distance(self, other: "Vec2") -> float:
        return (self - other).length()

    # Normalize & clamp
    def normalized(self) -> "Vec2":
        l = self.length()
        if l == 0:
            return Vec2(0, 0)
        return self / l

    def with_length(self, L: float) -> "Vec2":
        return self.normalized() * L

    def clamp_length(self, max_len: float) -> "Vec2":
        l2 = self.length_sq()
        if l2 > max_len * max_len and l2 > 0:
            return self.with_length(max_len)
        return Vec2(self.x, self.y)

    # Geometry helpers
    def dot(self, other: "Vec2") -> float:
        return self.x * other.x + self.y * other.y

    def perp(self) -> "Vec2":  # 2D perpendicular (left-hand)
        return Vec2(-self.y, self.x)

    def rotate(self, radians: float) -> "Vec2":
        c, s = math.cos(radians), math.sin(radians)
        return Vec2(self.x * c - self.y * s, self.x * s + self.y * c)

    def tuple(self) -> Tuple[float, float]:
        return (self.x, self.y)


# ---------------------------
#  Integrator utilities
# ---------------------------
@dataclass
class Kinematics:
    pos: Vec2
    vel: Vec2


@dataclass
class Dynamics:
    mass: float = 1.0
    max_speed: float = 220.0  # px/s
    max_force: float = 400.0  # N (px/s^2 * mass)


def integrate_semi_implicit_euler(kin: Kinematics, force: Vec2, dyn: Dynamics, dt: float) -> None:
    """v_{t+dt} = v_t + a*dt; x_{t+dt} = x_t + v_{t+dt}*dt"""
    # F = m a → a = F / m
    acc = force / dyn.mass
    new_vel = kin.vel + acc * dt
    # Clamp speed
    if new_vel.length_sq() > dyn.max_speed * dyn.max_speed:
        new_vel = new_vel.with_length(dyn.max_speed)
    kin.vel = new_vel
    kin.pos = kin.pos + kin.vel * dt


# ---------------------------
#  Steering behaviours
# ---------------------------
class Steering:
    @staticmethod
    def seek(current_pos: Vec2, current_vel: Vec2, target: Vec2, dyn: Dynamics) -> Vec2:
        desired = (target - current_pos).with_length(dyn.max_speed)
        steer = desired - current_vel
        return steer.clamp_length(dyn.max_force)

    @staticmethod
    def flee(current_pos: Vec2, current_vel: Vec2, threat: Vec2, dyn: Dynamics, panic_radius: float = 9999) -> Vec2:
        if current_pos.distance(threat) > panic_radius:
            return Vec2()
        desired = (current_pos - threat).with_length(dyn.max_speed)
        steer = desired - current_vel
        return steer.clamp_length(dyn.max_force)

    @staticmethod
    def arrive(current_pos: Vec2, current_vel: Vec2, target: Vec2, dyn: Dynamics, slowing_radius: float = 120.0) -> Vec2:
        to_target = target - current_pos
        dist = to_target.length()
        if dist == 0:
            return Vec2()
        # scale speed down as we get closer
        ramped = dyn.max_speed * (dist / slowing_radius)
        clipped = min(ramped, dyn.max_speed)
        desired = to_target.with_length(clipped)
        steer = desired - current_vel
        return steer.clamp_length(dyn.max_force)

    @staticmethod
    def wander(current_pos: Vec2, current_vel: Vec2, dyn: Dynamics, state: Dict) -> Vec2:
        """Classic wander: project a circle ahead and jitter the target on the circle."""
        # state contains: wand_angle, circle_dist, circle_radius, jitter
        wand_angle: float = state.setdefault("angle", 0.0)
        circle_dist: float = state.setdefault("dist", 40.0)
        circle_radius: float = state.setdefault("radius", 25.0)
        jitter: float = state.setdefault("jitter", 60.0)  # radians/sec randomization scale

        # forward direction (if stopped, pick any forward)
        forward = current_vel.normalized() if current_vel.length_sq() > 1e-6 else Vec2(1, 0)

        # random angular jitter
        wand_angle += (random.random() - 0.5) * 2.0 * (jitter * (1/60.0))  # small step per frame-ish; will be scaled via desired
        state["angle"] = wand_angle

        # center of circle ahead of the agent
        circle_center = current_pos + forward.with_length(circle_dist)
        # displacement on circle
        displacement = Vec2(math.cos(wand_angle), math.sin(wand_angle)) * circle_radius
        wander_target = circle_center + displacement

        # steer towards wander target
        desired = (wander_target - current_pos).with_length(dyn.max_speed)
        steer = (desired - current_vel).clamp_length(dyn.max_force)
        return steer

    @staticmethod
    def pursue(evader_pos: Vec2, evader_vel: Vec2, pursuer_pos: Vec2, pursuer_vel: Vec2, dyn: Dynamics) -> Vec2:
        # Predict time to reach current evader position based on relative speed
        to_evader = evader_pos - pursuer_pos
        rel_speed = max(1e-5, (dyn.max_speed + evader_vel.length()))
        t = to_evader.length() / rel_speed
        predicted = evader_pos + evader_vel * t
        return Steering.seek(pursuer_pos, pursuer_vel, predicted, dyn)


# ---------------------------
#  Agent & World
# ---------------------------
class Agent:
    def __init__(self, pos: Vec2, color: Tuple[int, int, int] = (200, 240, 255)):
        self.kin = Kinematics(pos=Vec2(pos.x, pos.y), vel=Vec2())
        self.dyn = Dynamics(mass=1.0, max_speed=220.0, max_force=420.0)
        self.color = color
        self.radius = 8

        # behaviour weights
        self.weights: Dict[str, float] = {
            "seek": 1.0,
            "flee": 1.0,
            "arrive": 1.0,
            "wander": 1.0,
            "pursue": 1.0,
        }
        # behaviour state (e.g., wander state)
        self.state: Dict[str, Dict] = {"wander": {}}

    def steering(self, inputs: Dict) -> Vec2:
        force = Vec2()
        # Sum forces (you can add priority-based later)
        if target := inputs.get("seek"):
            force += self.weights["seek"] * Steering.seek(self.kin.pos, self.kin.vel, target, self.dyn)
        if threat := inputs.get("flee"):
            force += self.weights["flee"] * Steering.flee(self.kin.pos, self.kin.vel, threat, self.dyn, panic_radius=300)
        if arrive_t := inputs.get("arrive"):
            force += self.weights["arrive"] * Steering.arrive(self.kin.pos, self.kin.vel, arrive_t, self.dyn, slowing_radius=inputs.get("arrive_slow", 120.0))
        if inputs.get("wander", False):
            force += self.weights["wander"] * Steering.wander(self.kin.pos, self.kin.vel, self.dyn, self.state["wander"])
        if pursue_t := inputs.get("pursue"):
            evader_pos, evader_vel = pursue_t
            force += self.weights["pursue"] * Steering.pursue(evader_pos, evader_vel, self.kin.pos, self.kin.vel, self.dyn)
        # Clamp total force
        return force.clamp_length(self.dyn.max_force)

    def update(self, inputs: Dict, dt: float):
        force = self.steering(inputs)
        integrate_semi_implicit_euler(self.kin, force, self.dyn, dt)

    def draw(self, surf: pygame.Surface, debug: bool = False):
        # Draw as a triangle pointing to velocity
        pos = self.kin.pos
        vel = self.kin.vel
        forward = vel.normalized() if vel.length_sq() > 1e-6 else Vec2(1, 0)
        left = forward.perp()
        tip = pos + forward.with_length(self.radius * 1.8)
        base_left = pos - forward.with_length(self.radius * 1.0) + left.with_length(self.radius * 0.9)
        base_right = pos - forward.with_length(self.radius * 1.0) - left.with_length(self.radius * 0.9)
        pygame.draw.polygon(surf, self.color, [tip.tuple(), base_left.tuple(), base_right.tuple()], 0)

        if debug:
            # velocity vector
            pygame.draw.line(surf, (100, 180, 255), pos.tuple(), (pos + forward.with_length(35)).tuple(), 1)


class World:
    def __init__(self, width: int = 960, height: int = 600):
        pygame.init()
        pygame.display.set_caption("Steering Behaviours (na mão)")
        self.screen = pygame.display.set_mode((width, height))
        self.width, self.height = width, height
        self.clock = pygame.time.Clock()

        self.wrap = True
        self.debug = True
        self.paused = False

        # Agents
        self.player = Agent(Vec2(width * 0.5, height * 0.5), color=(255, 245, 180))
        self.evader = Agent(Vec2(width * 0.2, height * 0.2), color=(200, 255, 200))
        self.evader.dyn.max_speed = 160

        # Behaviour mode
        self.mode = "wander"  # seek|flee|arrive|wander|pursue
        self.arrive_slow = 120.0
        self.wander_jitter = 60.0  # exposed to +/- keys

    def handle_events(self) -> bool:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return False
            if e.type == pygame.KEYDOWN:
                if e.key in (pygame.K_ESCAPE, pygame.K_q):
                    return False
                if e.key == pygame.K_SPACE:
                    self.paused = not self.paused
                if e.key == pygame.K_d:
                    self.debug = not self.debug
                if e.key == pygame.K_w:
                    self.wrap = not self.wrap
                if e.key == pygame.K_1:
                    self.mode = "seek"
                if e.key == pygame.K_2:
                    self.mode = "flee"
                if e.key == pygame.K_3:
                    self.mode = "arrive"
                if e.key == pygame.K_4:
                    self.mode = "wander"
                if e.key == pygame.K_5:
                    self.mode = "pursue"
                if e.key == pygame.K_PLUS or e.key == pygame.K_EQUALS:
                    self.wander_jitter = min(240.0, self.wander_jitter + 10.0)
                if e.key == pygame.K_MINUS:
                    self.wander_jitter = max(5.0, self.wander_jitter - 10.0)
                if e.key == pygame.K_LEFT:
                    self.arrive_slow = max(10.0, self.arrive_slow - 10.0)
                if e.key == pygame.K_RIGHT:
                    self.arrive_slow = min(300.0, self.arrive_slow + 10.0)
        return True

    def world_bounds(self, agent: Agent):
        if self.wrap:
            if agent.kin.pos.x < 0:
                agent.kin.pos.x += self.width
            elif agent.kin.pos.x > self.width:
                agent.kin.pos.x -= self.width
            if agent.kin.pos.y < 0:
                agent.kin.pos.y += self.height
            elif agent.kin.pos.y > self.height:
                agent.kin.pos.y -= self.height
        else:
            # bounce
            if agent.kin.pos.x < 0 or agent.kin.pos.x > self.width:
                agent.kin.vel.x *= -1
                agent.kin.pos.x = max(0, min(self.width, agent.kin.pos.x))
            if agent.kin.pos.y < 0 or agent.kin.pos.y > self.height:
                agent.kin.vel.y *= -1
                agent.kin.pos.y = max(0, min(self.height, agent.kin.pos.y))

    def render_hud(self):
        font = pygame.font.SysFont("consolas", 16)
        txt = (
            f"Mode: {self.mode.upper()}  | Wrap: {'ON' if self.wrap else 'OFF'}  | "
            f"ArriveSlow: {self.arrive_slow:.0f}  | WanderJitter: {self.wander_jitter:.0f}  | "
            f"Player v={self.player.kin.vel.length():.1f}"
        )
        surf = font.render(txt, True, (230, 230, 240))
        self.screen.blit(surf, (8, 8))

    def step(self, dt: float):
        # Update evader (simple wander so pursue has something to chase)
        self.evader.state["wander"].setdefault("jitter", self.wander_jitter)
        self.evader.state["wander"]["jitter"] = self.wander_jitter
        self.evader.update({"wander": True}, dt)
        self.world_bounds(self.evader)

        # Player inputs by mode
        mouse_pos = Vec2(*pygame.mouse.get_pos())
        inputs: Dict = {}
        if self.mode == "seek":
            inputs["seek"] = mouse_pos
        elif self.mode == "flee":
            inputs["flee"] = mouse_pos
        elif self.mode == "arrive":
            inputs["arrive"] = mouse_pos
            inputs["arrive_slow"] = self.arrive_slow
        elif self.mode == "wander":
            self.player.state["wander"].setdefault("jitter", self.wander_jitter)
            self.player.state["wander"]["jitter"] = self.wander_jitter
            inputs["wander"] = True
        elif self.mode == "pursue":
            inputs["pursue"] = (self.evader.kin.pos, self.evader.kin.vel)

        self.player.update(inputs, dt)
        self.world_bounds(self.player)

    def draw(self):
        self.screen.fill((10, 12, 16))
        # draw agents
        self.evader.draw(self.screen, debug=self.debug)
        self.player.draw(self.screen, debug=self.debug)
        if self.debug:
            # draw mouse target for seek/arrive/flee
            if self.mode in ("seek", "arrive", "flee"):
                pygame.draw.circle(self.screen, (255, 120, 120), pygame.mouse.get_pos(), 5, 1)
        self.render_hud()
        pygame.display.flip()

    def run(self):
        while True:
            if not self.handle_events():
                break
            dt = self.clock.tick(120) / 1000.0  # seconds
            if not self.paused:
                self.step(dt)
            self.draw()
        pygame.quit()


def main():
    world = World(960, 600)
    world.run()


if __name__ == "__main__":
    main()
