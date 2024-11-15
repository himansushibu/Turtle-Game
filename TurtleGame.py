import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Turtle Game")
wn.bgcolor("lightblue")
wn.setup(width=600, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

# Create the target turtle
target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.speed(0)
target.goto(random.randint(-290, 290), random.randint(-290, 290))


# Player movement functions
def move_up():
    y = player.ycor()
    if y < 290:
        player.sety(y + 20)


def move_down():
    y = player.ycor()
    if y > -290:
        player.sety(y - 20)


def move_left():
    x = player.xcor()
    if x > -290:
        player.setx(x - 20)


def move_right():
    x = player.xcor()
    if x < 290:
        player.setx(x + 20)


# Keyboard bindings
wn.listen()
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")

# Main game loop
while True:
    # Check for collision with the target
    if player.distance(target) < 20:
        # Move the target to a random spot
        target.goto(random.randint(-290, 290), random.randint(-290, 290))

    # Update the screen
    wn.update()
