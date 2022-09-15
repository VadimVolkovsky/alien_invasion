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
        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_width, self.settings.screen_height))  # Оконный режим
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # полноэкранный режим
        self.settings.screen_width = self.screen.get_rect().width  # обновляем ширину экрана
        self.settings.screen_height = self.screen.get_rect().height  # обновляем высоту экрана
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self.screen, self.settings)
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
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # если клавиша отпущена (UP)
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:  # если нажата стрелка вправо
            self.ship.moving_right = True  # непрерывное движение вправо
        elif event.key == pygame.K_LEFT:  # если нажата стрелка влево
            self.ship.moving_left = True  # непрерывное движение влево
        # elif event.key == pygame.K_UP:  # движение вверх
        #     self.ship.moving_up = True
        # elif event.key == pygame.K_DOWN:  # движение вниз
        #     self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  # остановка движения вправо
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False  # остановка движения влево
        # elif event.key == pygame.K_UP:  # остановка движения вверх
        #     self.ship.moving_up = False
        # elif event.key == pygame.K_DOWN:  # остановка движения вниз
        #     self.ship.moving_down = False



    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.person.blitme()
        pygame.display.flip()
    
    
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()