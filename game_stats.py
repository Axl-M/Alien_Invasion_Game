class GameStats:
    """ Отслеживание статистики для игры """
    def __init__(self, ai_settings):
        """ Инициализация статистики """
        self.ai_settings = ai_settings
        self.reset_stats()
        # Игра Alien Invasion запускается в НЕактивном состоянии.
        self.game_active = False
        # Рекорд не должен сбрасываться.
        self.high_score = 0

    def reset_stats(self):
        """ Инициализирует статистику, изменяющуюся в ходе игры. """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0  # Чтобы счет сбрасывался при запуске новой игры
        self.level = 1

