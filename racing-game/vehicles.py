class Car:
    def __init__(self):
        self.speed = 0
        self.odometer = 0
        self.time = 0
        self.maximumSpeed = 200

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 10

    def step(self):
        self.odometer += self.speed
        self.time += 1