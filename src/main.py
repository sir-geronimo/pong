import sys
from typing import List, Union, Dict

import pygame
from pygame.locals import *
from pygame.mixer import Sound
from pygame.surface import Surface, SurfaceType
from pygame.time import Clock

from constants.window import SCREEN_HEIGHT, SCREEN_WIDTH, CENTER_HEIGHT, CENTER_WIDTH
from entities.ball import Ball
from entities.entity import Entity
from entities.player import Player

# -------------
# init
# -------------
pygame.mixer.pre_init()
pygame.init()


# -------------
# constants
# -------------
player_size = (10, 125)
background_color = pygame.Color('grey10')
primary_color = (175, 175, 175)

font = pygame.font.SysFont('Arial', 32)
small_font = pygame.font.SysFont('Arial', 24)


class Main:
    is_running: bool = False
    is_paused: bool = False
    screen: Union[Surface, SurfaceType]
    clock: Clock
    entities: List[Entity]
    ball: Ball
    players: Dict[str, Player] = {}
    points: Dict[str, int] = {
        "player_1": 0,
        "player_2": 0
    }
    score_sfx: Sound

    def __init__(self):
        pygame.display.set_caption("My awesome pong game")

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.is_running = True
        self.__load_entities()
        self.__load_resources()

    def run(self):
        while self.is_running:
            if self.is_paused:
                self.__new_match()

            if not self.is_paused:
                [entity.__update__() for entity in self.entities]

                self.__draw_visuals()
                self.__move_ball()

            self.__check_events()
            self.clock.tick(75)
            pygame.display.flip()

    def __draw_visuals(self):
        self.screen.fill(background_color)

        pygame.draw.aaline(
            self.screen,
            primary_color,
            (CENTER_WIDTH, 0),
            (CENTER_WIDTH, SCREEN_HEIGHT)
        )

        scoreboard = small_font.render(
            f"{self.points['player_2']}     {self.points['player_1']}",
            True,
            primary_color
        )
        centered_scoreboard = CENTER_WIDTH - scoreboard.get_width()/2
        self.screen.blit(scoreboard, (centered_scoreboard, CENTER_HEIGHT))

        pygame.draw.ellipse(self.screen, primary_color, self.ball)

        [pygame.draw.rect(self.screen, primary_color, player) for player in self.players.values()]

    def __check_events(self):
        for event in pygame.event.get():
            # Quit game
            if event.type == pygame.QUIT:
                self.is_running = False
                pygame.quit()
                sys.exit()

            # Continue game
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    self.is_paused = not self.is_paused

    def __move_ball(self):
        [self.ball.collide(player) for player in self.players.values()]

        if self.ball.left <= 0:
            self.points["player_1"] += 1
            self.score_sfx.play()
        if self.ball.right >= SCREEN_WIDTH:
            self.points["player_2"] += 1
            self.score_sfx.play()

    def __load_entities(self):
        self.ball = Ball(
            position=(SCREEN_WIDTH / 2 - 15, CENTER_HEIGHT - 15)
        )

        self.players = {
            "player_1": Player(
                keys={
                    "up": K_UP,
                    "down": K_DOWN,
                },
                position=(SCREEN_WIDTH - 20, CENTER_HEIGHT - 70),
                size=player_size
            ),
            "player_2": Player(
                keys={
                    "up": K_w,
                    "down": K_s,
                },
                position=(10, CENTER_HEIGHT - 70),
                size=player_size
            )
        }

        self.entities = [
            self.players["player_1"],
            self.players["player_2"],
            self.ball,
        ]

    def __pause(self):
        self.is_paused = True

    def __new_match(self):
        pause_text = font.render(
            "Paused, press space key to continue...",
            True,
            primary_color,
            background_color
        )
        centered_text = CENTER_WIDTH - pause_text.get_width()/2
        self.screen.blit(pause_text, (centered_text, CENTER_HEIGHT))

    def __load_resources(self):
        # Sound Effects
        self.score_sfx = pygame.mixer.Sound("../resources/sfx/score.wav")


if __name__ == "__main__":
    game = Main()
    game.run()
