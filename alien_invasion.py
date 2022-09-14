import sys

import pygame


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""
    
    def __init__(self) -> None:
        pygame.init

        self.screen = pygame.display.set_mode((1200, 800)) # Размер игрового окна
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            # Отслеживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # При каждом проходе цикла перерисовывается экран
            self.screen.fill(self.bg_color)

            # отображение последнего прорисованного экрана.
            pygame.display.flip()
    
    
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()