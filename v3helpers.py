from turtle import Turtle
import random

# head class
class Head(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.color("white")
        self.shape("square")
        self.speed(0)
        self.direction = "stop"
        self.penup()
        self.goto(0, 100)

    # def functions to change direction of head

    def go_up(self):
        if self.direction != "down":
            self.direction = "up"

    def go_down(self):
        if self.direction != "up":
            self.direction = "down"

    def go_left(self):
        if self.direction != "right":
            self.direction = "left"

    def go_right(self):
        if self.direction != "left":
            self.direction = "right"

    # move towards the direction head is facing

    def move(self):
        if self.direction == "up":
            x, y = self.xcor(), self.ycor()
            self.goto(x + 0, y + 20)

        if self.direction == "down":
            x, y = self.xcor(), self.ycor()
            self.goto(x + 0, y - 20)

        if self.direction == "left":
            x, y = self.xcor(), self.ycor()
            self.goto(x + -20, y + 0)

        if self.direction == "right":
            x, y = self.xcor(), self.ycor()
            self.goto(x + 20, y + 0)

    def reset_head(self):
        self.goto(0, 100)
        self.direction = "stop"
        self.speed(0)

# body class
class Body(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.color("yellow")
        self.shape("square")
        self.speed(0)
        self.penup()

# food class
class Food(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.color("blue")
        self.shape("circle")
        self.speed(0)
        self.penup()
        #self.goto(0, 0)

    # food reinitialize at random spot
    def food_random(self):
        x, y = random.randint(-290, 290), random.randint(-290, 290)
        self.goto(x, y)


# pen class
class Pen(Turtle):
    def __init__(self, high_score):
        Turtle.__init__(self)
        self.goto(0, 330)
        self.color("white")
        self.shape("square")
        self.penup()
        self.hideturtle()
        self.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Arial", 24, "normal"))

    def update_score(self, score, high_score):
        self.clear()
        self.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "normal"))
