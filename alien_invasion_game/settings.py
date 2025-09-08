class Settings:
    """Uma classe que armazena todas as configurações do Jogo."""

    def __init__(self):
        """Inicializa as configurações do jogo."""

        # screen
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_size = (self.screen_width, self.screen_height)

        # cores
        self.bg_color = (230, 230, 230)

        self.ship_speed = 2.0

        # bullet
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 6
