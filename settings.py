class Settings():
    """ Класс для хранения всех настроек игры """

    def __init__(self):
        # параметры экрана
        self.screen_width = 1200
        self.screen_height = 750
        # цвет фона
        self.bg_color = (230, 230, 230)

        # настройки корабля
        self.ship_speed_factor = 1.5

        # параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bulets_allowed = 3

        # настройки пришельцев
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1