import pygame

class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings

        self.screen_rect = game.screen.get_rect()

        sprite = pygame.image.load('assets/ship.png')
        self.image = pygame.transform.scale(sprite, (128, 128))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False


    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on movement flags"""
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

