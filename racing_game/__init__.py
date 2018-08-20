import pygame
import math
import time
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
    k_left = k_right = k_down = 0

    game_is_running = True  # Sets the game to start

    # Generates and draws the player car object
    player = Car(position, "./racing_game/assets/logo32x32.png", 7, 0, 0.1, 30)

    while game_is_running:
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
                k_left = pressed_down * player.turn_speed  # Shifts the car to the left
            elif event.key == K_RIGHT:
                k_right = pressed_down * player.turn_speed  # Shifts the car to the right
            elif event.key == K_DOWN:
                k_down = pressed_down * player.acceleration * 2  # Shifts the car backwards
            '''
            # Enable this, if auto-acceleration is disabled
            elif event.key == K_UP:
                k_up = pressed_down * player.acceleration  # Shifts the car forward
            '''

        # [TEMP] - Makes the screen black
        screen.fill(background)

        print(player.speed)
        # Speed acceleration algorithm
        player.speed += (player.acceleration - k_down)  # Calculates the forward/backward speed
        player.direction += (k_left - k_right)  # Changes the turn direction of the car
        if player.speed > player.maximum_forward_speed:
            player.speed = player.maximum_forward_speed  # Limits the maximum forward speed
        elif player.speed < player.maximum_backward_speed:
            player.speed = player.maximum_backward_speed  # Limits the maximum backward speed

        # Generates new position based on current position, speed and direction

        player_x, player_y = position
        rad = player.direction * math.pi / 180
        player_x -= player.speed * math.sin(rad)
        player_y -= player.speed * math.cos(rad)

        # Making sure the car doesn't go out of bounds
        if player_x < 0:
            player_x = 0
        elif player_x > windowSettings["width"]:
            player_x = windowSettings["width"]  # Prevents from the exiting from the x-axis

        if player_y < windowSettings["height"] / 1.8:
            player_y = windowSettings["height"] / 1.8
        elif player_y > windowSettings["height"]:
            player_y = windowSettings["height"]  # Prevents from the exiting from the y-axis

        # Updates the current player position
        position = (player_x, player_y)

        # Rotates the car image for direction of the arrow pressed
        rotated = pygame.transform.rotate(player.car, player.direction)

        # Positioning the car on the active screen
        rect = rotated.get_rect()
        rect.center = position

        # Renders the car object to screen
        screen.blit(rotated, rect)
        pygame.display.flip()

        # DEBUG Segment
        print(player.speed)

        # Variable reset statements
        player.direction = 0  # Prevents the car from spinning

        # Sets the game screen to update 120 times per second (because PC master race, b***h :D)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(120)
