from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        rand_no = random.randint(1, 6)
        if rand_no == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            rand_y = random.randint(-250, 250)
            new_car.goto(300, rand_y)
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

