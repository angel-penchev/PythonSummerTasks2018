import pygame
import math
from pygame.locals import *
from .constants import windowSettings
from .classes import Car


def main():
    pygame.init()  # Initializing the pygame module

    # Defining game window logo & title
    logo = pygame.image.load(windowSettings["logoPath"])
    pygame.display.set_icon(logo)
    pygame.display.set_caption(windowSettings["caption"])

    # Defining the game window width & height, as well as the background color
    screen = pygame.display.set_mode((windowSettings["width"], windowSettings["height"]))
    background = (0, 0, 0)

    # Defining the game clock feature
    clock = pygame.time.Clock()

    # Sets player default position
    position = (windowSettings["width"] / 2, windowSettings["height"] - (Car.height + 30))
    k_left = k_right = k_up = k_down = 0

    game_is_running = True  # Sets the game to start

    while game_is_running:
        # Generates and draws the player car object
        player = Car(position, "./racing_game/assets/logo32x32.png", 10, -2, 1, 30)

        for event in pygame.event.get():
            # Defining game "QUIT" function
            if event.type == pygame.QUIT:
                game_is_running = False

            # Defining the event key
            if not hasattr(event, 'key'):
                continue

            # Defining a event key-down variable
            pressed_down = event.type == KEYDOWN

            # Gets the pressed key user input and moves the car
            if event.key == K_LEFT:
                player.direction = -45
                k_left = pressed_down * player.turn_speed  # Shifts the car to the left
            elif event.key == K_RIGHT:
                player.direction = 45
                k_right = pressed_down * player.turn_speed  # Shifts the car to the right
            elif event.key == K_UP:
                player.direction = 0
                k_up = pressed_down * player.acceleration  # Shifts the car forward
            elif event.key == K_DOWN:
                player.direction = 0
                k_down = pressed_down * player.acceleration  # Shifts the car backwards

        # [TEMP] - Makes the screen black
        screen.fill(background)

        # Speed acceleration algorithm
        player.speed += (k_up - k_down)
        if player.speed > player.maximum_forward_speed:
            player.speed = player.maximum_forward_speed  # Limits the maximum forward speed
        elif player.speed < player.maximum_backward_speed:
            player.speed = player.maximum_backward_speed  # Limits the maximum backward speed
        player.direction += (k_left - k_right)

        # .. new position based on current position, speed and direction
        player_x, player_y = position
        rad = player.direction * math.pi / 180
        player_x -= player.speed * math.sin(rad)
        player_y -= player.speed * math.cos(rad)

        #
        if player_x < 0:
            player_x = 0
        elif player_x > windowSettings["width"]:
            player_x = windowSettings["width"]

        # make sure the car doesn't exit the screen
        if player_y < 0:
            player_y = 0
        elif player_y > windowSettings["height"]:
            player_y = windowSettings["height"]

        # Updates the current player position
        position = (player_x, player_y)

        # Rotates the car image for direction of the arrow pressed
        rotated = pygame.transform.rotate(player.car, player.direction)

        # .. position the car on screen
        rect = rotated.get_rect()
        rect.center = position

        # Renders the car object to screen
        screen.blit(rotated, rect)
        pygame.display.flip()

        # Sets the game screen to update 120 times per second (because PC master race, b***h :D)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(120)
