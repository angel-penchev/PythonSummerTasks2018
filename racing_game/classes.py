import pygame


class Car:
    # Car size variables
    width = 32
    height = 32

    def __init__(self, position, model, maximum_forward_speed, maximum_backward_speed, acceleration, turn_speed):

        # Speed & direction variables
        self.speed = 0
        self.direction = 0
        self.position = position
        self.maximum_forward_speed = maximum_forward_speed
        self.maximum_backward_speed = maximum_backward_speed

        # Acceleration/Turn_speed variables
        self.acceleration = acceleration
        self.turn_speed = turn_speed

        # Car appearance variables
        self.type = model

        self.car = pygame.image.load(model)

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 10


class Obstacle:
    def __init__(self):
        self.damage = 0
        self.speedDecrease = 0
