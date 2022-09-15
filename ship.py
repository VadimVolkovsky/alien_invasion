import pygame


class Ship():
    """Класс для управления кораблем"""
    def __init__(self, ai_game_screen, ai_game_settings):
        """Инициализирует корабль и задает его начальную позицию"""
        self.screen = ai_game_screen
        self.settings = ai_game_settings
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/ship_1.bmp')  # Загружает изображение корабля
        self.rect = self.image.get_rect()  # и получает прямоугольник.
        self.rect.midbottom = self.screen_rect.midbottom  # каждый новый корабль появляется у нижнего края экрана
        self.x = float(self.rect.x) # сохранение вещественной координаты корабля
        self.moving_right = False  # Флаг перемещения корабля вправо
        self.moving_left = False  # Флаг перемещения корабля влево

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x  # обновление атрибута rect на основании self.x
    
    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)