import pygame
import math


class Car:
    # Car size variables
    width = 32
    height = 32

    def __init__(self, position, model, maximum_forward_speed, maximum_backward_speed, acceleration, turn_speed):

        # Speed & direction variables
        self.speed = 0
        self.direction = 0
        self.position = position
        self.x, self.y = position
        self.maximum_forward_speed = maximum_forward_speed
        self.maximum_backward_speed = maximum_backward_speed

        # Acceleration/Turn_speed variables
        self.acceleration = acceleration
        self.turn_speed = turn_speed

        # Car appearance variables
        self.type = model

        self.car = pygame.image.load(model)

    def drive(self, k_left, k_right, k_down):
        # Speed acceleration algorithm
        self.speed += (self.acceleration - k_down)  # Calculates the forward/backward speed
        self.direction += (k_left - k_right)  # Changes the turn direction of the car

        if self.speed > self.maximum_forward_speed:
            self.speed = self.maximum_forward_speed  # Limits the maximum forward speed
        elif self.speed < self.maximum_backward_speed:
            self.speed = self.maximum_backward_speed  # Limits the maximum backward speed

        # Generates new position based on current position, speed and direction
        rad = self.direction * math.pi / 180
        self.x -= self.speed * math.sin(rad)
        self.y -= self.speed * math.cos(rad)


class Obstacle:
    def __init__(self):
        self.damage = 0
        self.speedDecrease = 0
