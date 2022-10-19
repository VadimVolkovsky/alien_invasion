import pygame
from pygame.sprite import Sprite


class Meteor(Sprite):
    """Класс для одного метеора"""
    
    def __init__(self, ai_game) -> None:
        """Создает метеор и задает его первоначальную позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/meteor_1.bmp')  #  изображение метеора
        self.rect = self.image.get_rect()  #  создание прямоугольника
        
        # каждый новый метеор появляется в верхнем левом углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной вертикальной позиции метеора
        self.y = float(self.rect.y)

    # def check_edges(self):
    #     """Возвращает True, если метеор находится у края экрана"""
    #     screen_rect = self.screen.get_rect()
    #     if self.rect.bottom >= screen_rect.bottom:  # если достигнут нижний кран экрана
    #         return True
    
    def update(self):
        """Перемещает метеоры вниз по экрану (по оси у)"""
        self.y += self.settings.meteor_speed
        self.rect.y = self.y

        
