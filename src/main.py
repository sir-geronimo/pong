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

player_size = (10, 125)
player_speed = 0

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
    x_speed = 10
    y_speed = 10
    size = (30, 30)
    
    def __init__(self, position):
        super().__init__(position, self.size)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed
    
    def bounce(self):
        if self.top <=0 or self.bottom >= SCREEN_HEIGHT:
            self.y_speed *= -1
        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            self.x_speed *= -1
    
    def collide(self):
        if ball.colliderect(player) or ball.colliderect(opponent):
            self.x_speed *= -1

class Player(Rect):
    pass



# -------------
# Game rectangles
# -------------
ball = Ball((SCREEN_WIDTH/2 - 15, SCREEN_HEIGHT/2 - 15))

player = pygame.Rect(
    (SCREEN_WIDTH - 20, SCREEN_HEIGHT/2 - 70),
    player_size
)

opponent = pygame.Rect(
    (10, SCREEN_HEIGHT/2 - 70),
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
    ball.collide()

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
        (SCREEN_WIDTH/2, 0),
        (SCREEN_WIDTH/2, SCREEN_HEIGHT)
    )


    # Update screen
    pygame.display.update()
    clock.tick(75)
# -------------
