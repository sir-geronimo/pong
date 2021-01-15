import sys
import pygame
from pygame.locals import *

# -------------
# General setup
# -------------
pygame.init()
clock = pygame.time.Clock()
# -------------


# -------------
# constants
# -------------
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 980

half_screen_height = SCREEN_HEIGHT/2
half_screen_width = SCREEN_WIDTH/2
screen_center = (half_screen_width, half_screen_height)

player_size = (10, 125)
player_speed = 0

ball_size = (30, 30)
ball_speed_x = 5
ball_speed_y = 5

bg_color = pygame.Color('grey10')
obj_color = (175, 175, 175)
# -------------


# -------------
# Setting up main window
# -------------
pygame.display.set_caption("My awesome game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# -------------


class Ball(Rect):
    x_speed = 5
    y_speed = 5
    
    def __init__(self, position, size):
        self = Rect(position, size)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed
    
    def bounce(self):
        if self.top <=0 or self.bottom >= SCREEN_HEIGHT:
            self.y_speed *= -1
        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            self.x_speed *= -1


# -------------
# Game rectangles
# -------------
ball = Ball(
    (half_screen_width - 15, half_screen_height - 15),
    ball_size
)

player = pygame.Rect(
    (SCREEN_WIDTH - 20, half_screen_height - 70),
    player_size
)

opponent = pygame.Rect(
    (10, half_screen_height - 70),
    player_size
)
# -------------


# -------------
# Main loop
# -------------
while True:
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 7
            if event.key == pygame.K_DOWN:
                player_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 7
            if event.key == pygame.K_DOWN:
                player_speed -= 7
    ball.move()
    ball.bounce()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >=SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT
        
    # Visuals
    screen.fill(bg_color)

    pygame.draw.ellipse(screen, obj_color, ball)
    pygame.draw.rect(screen, obj_color, player)
    pygame.draw.rect(screen, obj_color, opponent)

    pygame.draw.aaline(
        screen,
        obj_color,
        (half_screen_width, 0),
        (half_screen_width, SCREEN_HEIGHT)
    )


    # Update screen
    pygame.display.flip()
    clock.tick(75)
# -------------
