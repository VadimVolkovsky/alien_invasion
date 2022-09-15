import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс для одного пришельца"""
    
    def __init__(self, ai_game) -> None:
        """Создает пришельца и задает его первоначальную позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('images/alien.bmp')  # загрузка изображения пришельца
        self.rect = self.image.get_rect()  #  создание прямоугольника
        
        # каждый новый пришелец появляется в верхнем левом углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной горизонтальной позиции пришельца
        self.x = float(self.rect.x)
