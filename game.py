import turtle
import time
import random

# Screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake body
body = []

# Score
score = 0
high_score = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)

def update_score():
    score_display.clear()
    score_display.write(
        f"Score: {score}  High Score: {high_score}",
        align="center",
        font=("Arial", 18, "normal")
    )

update_score()

# Movement functions
def up():
    if head.direction != "down":
        head.direction = "up"

def down():
    if head.direction != "up":
        head.direction = "down"

def left():
    if head.direction != "right":
        head.direction = "left"

def right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    if head.direction == "down":
        head.sety(head.ycor() - 20)

    if head.direction == "left":
        head.setx(head.xcor() - 20)

    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard controls
screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

# Main game loop
while True:
    screen.update()

    # Wall collision
    if (
        head.xcor() > 290 or
        head.xcor() < -290 or
        head.ycor() > 290 or
        head.ycor() < -290
    ):
        time.sleep(1)

        head.goto(0, 0)
        head.direction = "stop"

        for segment in body:
            segment.goto(1000, 1000)

        body.clear()

        score = 0
        update_score()

    # Food collision
    if head.distance(food) < 20:

        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()

        body.append(new_segment)

        score += 10

        if score > high_score:
            high_score = score

        update_score()

    # Move body from last segment
    for i in range(len(body) - 1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)

    # First segment follows head
    if len(body) > 0:
        body[0].goto(head.xcor(), head.ycor())

    move()

    # Collision with body
    for segment in body:
        if segment.distance(head) < 20:
            time.sleep(1)

            head.goto(0, 0)
            head.direction = "stop"

            for segment in body:
                segment.goto(1000, 1000)

            body.clear()

            score = 0
            update_score()

    time.sleep(0.1)

screen.mainloop()