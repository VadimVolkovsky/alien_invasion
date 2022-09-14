import sys

import pygame

from settings import Settings
from ship import Ship
from person import Person


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""
    def __init__(self) -> None:
        pygame.init
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) # Размер игрового окна
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self.screen)
        self.person = Person(self.screen)

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()  # Проверяет  действия юзера
            self.ship.update()  # Обновить статус корабля
            self._update_screen()  # Обновление экрана при каждом проходе цикла

    def _check_events(self):
        """Обрабатывает нажатия клавиш и мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # если клавиша нажата (DOWN)
                if event.key == pygame.K_RIGHT:  # если нажата клавиша "стрелка вправо"
                    self.ship.moving_right = True  # активируется непрерывное движение вправо
            elif event.type == pygame.KEYUP:  # если клавиша отпущена (UP)
                self.ship.moving_right = False  # остановка движения


    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.person.blitme()
        pygame.display.flip()
    
    
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()