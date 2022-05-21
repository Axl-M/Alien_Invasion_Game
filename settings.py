class Settings():
    """ Класс для хранения всех настроек игры """

    def __init__(self):
        """ Инициализирует статические настройки игры. """
        # параметры экрана
        self.screen_width = 1200
        self.screen_height = 750
        # цвет фона
        self.bg_color = (230, 230, 230)

        # настройки корабля
        self.ship_limit = 3 # будет 4 попытки

        # параметры пули
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bulets_allowed = 7

        # настройки пришельцев
        self.fleet_drop_speed = 10
        # темп ускорения игры
        self.speedup_scale = 1.1            # Увеличение сложности с каждым уровнем
        self.score_scale = 2                # Темп роста стоимости пришельцев
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Инициализирует настройки, изменяющиеся в ходе игры.
        сбрасываются в начале каждой новой игры"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 1
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
        self.alien_points = 10  # к-во очков за 1 уничтоженный корабль

    def increase_speed(self):
        """ Увеличивает настройки скорости (темп игры). """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)


