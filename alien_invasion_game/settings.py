class Settings:
    """Uma classe que armazena todas as configurações do Jogo."""

    def __init__(self):
        """Initialize the game's static settings."""

        # screen
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_size = (self.screen_width, self.screen_height)
        self.bg_color = (230, 230, 230)


        # bullet
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 6

        # alien
        self.fleet_drop_speed = 10


        # ship
        self.ship_limit = 3

        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):    
        """Initialize settings tha change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

