from typing import Dict, Tuple

import pygame

from constants.window import SCREEN_HEIGHT
from entities.entity import Entity


class Player(Entity):
    speed = 0
    keys: Dict[str, int] = {}

    def __init__(
            self, keys: Dict[str, int],
            position: Tuple[float, float],
            size: Tuple[int, int],
    ) -> None:
        super().__init__(position, size)
        self.keys = keys

    def __update__(self) -> None:
        self.__move_around()
        self.__check_boundaries()

    def __move_around(self) -> None:
        self.speed = 0
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[self.keys["up"]]:
            self.speed -= 10
        if pressed_keys[self.keys["down"]]:
            self.speed += 10

        self.y += self.speed

    def __check_boundaries(self) -> None:
        if self.top <= 0:
            self.top = 0

        if self.bottom >= SCREEN_HEIGHT:
            self.bottom = SCREEN_HEIGHT
