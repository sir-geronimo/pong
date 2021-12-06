import pygame
from typing import Tuple
from pygame.locals import *

from constants.window import SCREEN_HEIGHT, SCREEN_WIDTH
from entities.player import Player


class Ball(Rect):
    x_speed: int = 5
    y_speed: int = 5
    size: Tuple[float, float] = (30, 30)

    def __init__(
        self, position: Tuple[float, float],
    ) -> None:
        super().__init__(position, self.size)

    def update(self):
        self.move()
        self.bounce()

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def bounce(self):
        if self.top <= 0 or self.bottom >= SCREEN_HEIGHT:
            self.y_speed *= -1
        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            self.x_speed *= -1

    def collide(self, pad: Player):
        # Check for collision
        if self.colliderect(pad):
            self.x_speed *= -1
