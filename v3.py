from turtle import Turtle, Screen, done
from v3helpers import Head, Body, Food, Pen
import time
import math

def main():
    # set up screen

    win = Screen()
    win.setup(width = 800, height = 800)
    win.bgcolor("black")
    win.tracer(0)
    win.title("Hello Snake V3")

    # set up square border

    square = Turtle()
    square.pencolor("white")
    square.shape("square")
    square.shapesize(29, 29, 1)
    square.fillcolor("")

    # Initialize some variables
    segments = []
    delay = 0.1
    score = 0
    high_score = 0

    # set up variables as classes
    head = Head()
    food = Food()
    pen = Pen(high_score)

    # window to listen on click of WASD, and execute function to change direction of head

    win.listen()
    win.onkey(head.go_up, "W")
    win.onkey(head.go_down, "S")
    win.onkey(head.go_left, "A")
    win.onkey(head.go_right, "D")

    while True:

        # continously update the game

        win.update()
        time.sleep(delay)

        # if head touches food,
        if head.distance(food.pos()) < 15:

            # food reinitialize at random spot
            food.food_random()

            # body increases
            body = Body()
            segments.append(body)

            score += 10

            if score > high_score:
                high_score = score

            # update score
            pen.update_score(score, high_score)

            # make snake faster
            delay -= 0.001

        # put body to follow head
        for i in range(len(segments)-1, 0, -1):
            x, y = segments[i-1].xcor(), segments[i-1].ycor()
            segments[i].goto(x, y)

        if len(segments) > 0:
            x, y = head.xcor(), head.ycor()
            segments[0].goto(x, y)

        head.move()

        # if head touches wall, dies and game resets
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.reset_head()

            for j in segments:
                j.goto(1000, 1000)

            segments = []
            score = 0

            pen.update_score(score, high_score)


        # if head touches body, dies and game resets
        for k in segments:
            if head.distance(k) < 15:
                time.sleep(1)
                head.reset_head()

                for j in segments:
                    j.goto(1000, 1000)

                segments = []
                score = 0

                pen.update_score(score, high_score)

    done()

if __name__ == "__main__":
    main()
