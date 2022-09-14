import pygame


class Person():
    """Класс для управления персонажем"""
    def __init__(self, ai_game):
        """Инициализирует персонажа и задает его начальную позицию"""
        self.screen = ai_game
        self.screen_rect = ai_game.get_rect()

        # Загружает изображение персонажа и получает прямоугольник
        self.image = pygame.image.load('images/person.bmp')
        self.rect = self.image.get_rect()
        # каждый новый персонаж появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.center
    
    def blitme(self):
        """Рисует персонажа в текущей позиции"""
        self.screen.blit(self.image, self.rect)