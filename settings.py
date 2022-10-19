class Settings():
    """Класс для хранени настроек игры """
    
    def __init__(self) -> None:
        """Инициализирует настройки игры"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5  #  скорость перемещения корабля
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Fleet direction = 1 обозначет движение вправо; а -1 обозначает влево
        self.fleet_direction = 1
        self.meteor_speed = 1