import sys
from typing import List, Union, Dict

import pygame
from pygame.locals import *
from pygame.surface import Surface, SurfaceType
from pygame.time import Clock

from constants.window import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_CENTER
from entities.ball import Ball
from entities.entity import Entity
from entities.player import Player

# -------------
# constants
# -------------
player_size = (10, 125)
bg_color = pygame.Color('grey10')
obj_color = (175, 175, 175)


class Main:
    is_running: bool
    screen: Union[Surface, SurfaceType]
    clock: Clock
    entities: List[Entity]
    ball: Ball
    players: Dict[str, Player] = {}

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("My awesome pong game")

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.is_running = True
        self.__load_entities()

    def run(self):
        while self.is_running:
            [entity.__update__() for entity in self.entities]

            self.__draw_visuals()
            self.__check_events()
            self.__move_ball()

            pygame.display.update()
            self.clock.tick(75)

    def __draw_visuals(self):
        self.screen.fill(bg_color)

        pygame.draw.aaline(
            self.screen,
            obj_color,
            (SCREEN_WIDTH / 2, 0),
            (SCREEN_WIDTH / 2, SCREEN_HEIGHT)
        )

        pygame.draw.ellipse(self.screen, obj_color, self.ball)

        [pygame.draw.rect(self.screen, obj_color, player) for player in self.players.values()]

    def __check_events(self):
        for event in pygame.event.get():
            # Quit game
            if event.type == pygame.QUIT:
                self.is_running = False
                pygame.quit()
                sys.exit()

    def __move_ball(self):
        [self.ball.collide(player) for player in self.players.values()]

    def __load_entities(self):
        self.ball = Ball(
            position=(SCREEN_WIDTH / 2 - 15, SCREEN_CENTER - 15)
        )

        self.players = {
            "player_1": Player(
                keys={
                    "up": K_UP,
                    "down": K_DOWN,
                },
                position=(SCREEN_WIDTH - 20, SCREEN_CENTER - 70),
                size=player_size
            ),
            "player_2": Player(
                keys={
                    "up": K_w,
                    "down": K_s,
                },
                position=(10, SCREEN_CENTER - 70),
                size=player_size
            )
        }

        self.entities = [
            self.ball,
        ]

        [self.entities.append(player) for player in self.players.values()]


if __name__ == "__main__":
    game = Main()
    game.run()
