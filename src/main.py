import sys
from typing import List, Union
import pygame
from pygame.locals import *
from constants.window import SCREEN_HEIGHT, SCREEN_WIDTH
from entities.ball import Ball
from entities.player import Player
from src.constants.window import SCREEN_CENTER

# -------------
# General setup
# -------------
pygame.init()
clock = pygame.time.Clock()

# -------------


# -------------
# constants
# -------------

player_size = (10, 125)

bg_color = pygame.Color('grey10')
obj_color = (175, 175, 175)

# -------------


# -------------
# Setting up main window
# -------------
pygame.display.set_caption("My awesome pong game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# -------------


# -------------
# Game rectangles
# -------------
ball = Ball(
    position=(SCREEN_WIDTH / 2 - 15, SCREEN_CENTER - 15)
)

player = Player(
    keys={
        "up": K_UP,
        "down": K_DOWN,
    },
    position=(SCREEN_WIDTH - 20, SCREEN_CENTER - 70),
    size=player_size
)

opponent = Player(
    keys={
        "up": K_w,
        "down": K_s,
    },
    position=(10, SCREEN_CENTER - 70),
    size=player_size
)

entities: List[Union[Player, Ball]] = [
    player,
    opponent,
    ball,
]

# -------------


# -------------
# Main loop
# -------------
while True:
    for e in entities:
        e.update()

    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball.move()
    ball.collide(player)
    ball.collide(opponent)

    # Visuals
    screen.fill(bg_color)

    pygame.draw.ellipse(screen, obj_color, ball)
    pygame.draw.rect(screen, obj_color, player)
    pygame.draw.rect(screen, obj_color, opponent)

    pygame.draw.aaline(
        screen,
        obj_color,
        (SCREEN_WIDTH / 2, 0),
        (SCREEN_WIDTH / 2, SCREEN_HEIGHT)
    )

    # Update screen
    pygame.display.update()
    clock.tick(75)

# -------------
