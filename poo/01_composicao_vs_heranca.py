# Tópico 1.5 — Composição vs Herança
#
# - Herança (IS-A): use quando a relação for "é-um" e você quer especializar.
# - Composição (HAS-A): use quando você quer montar objetos com partes, delegando responsabilidades.
#   Geralmente mais flexível e com menor acoplamento.

from __future__ import annotations
from typing import Protocol


# 1) Composição: Carro "tem-um" Motor
class Motor(Protocol):
    def ligar(self) -> str: ...
    def acelerar(self) -> str: ...


class MotorCombustao:
    def ligar(self) -> str:
        return "Motor a combustão ligado"

    def acelerar(self) -> str:
        return "Vrum!"


class MotorEletrico:
    def ligar(self) -> str:
        return "Motor elétrico ligado"

    def acelerar(self) -> str:
        return "Zzzzz!"


class Carro:
    def __init__(self, motor: Motor):
        # Dependência injetada: permite trocar o motor facilmente (flexibilidade)
        self.motor = motor

    def ligar(self) -> str:
        return self.motor.ligar()

    def acelerar(self) -> str:
        return self.motor.acelerar()


# 2) Herança: especializações
class Veiculo:
    def mover(self) -> str:
        return "Veículo se movendo"


class Moto(Veiculo):
    def mover(self) -> str:
        return "Moto acelerando em duas rodas"


class Caminhao(Veiculo):
    def mover(self) -> str:
        return "Caminhão puxando carga pesada"


def demo_composicao():
    print("\n[DEMO] Composição")
    carro_flex = Carro(MotorCombustao())
    carro_ev = Carro(MotorEletrico())
    print(carro_flex.ligar(), "-", carro_flex.acelerar())
    print(carro_ev.ligar(), "-", carro_ev.acelerar())


def demo_heranca():
    print("\n[DEMO] Herança")
    veiculos = [Veiculo(), Moto(), Caminhao()]
    for v in veiculos:
        print(v.mover())


# Diretrizes:
# - Prefira composição quando a especialização via herança não for clara.
# - Composição facilita testes (injeção de dependências) e extensões futuras.
# - Evite herança profunda (muitas camadas) e múltipla sem necessidade.


if __name__ == "__main__":
    demo_composicao()
    demo_heranca()

