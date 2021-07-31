import turtle

window = turtle.Screen()
window.title("Pong for learning")
window.bgcolor("black")
window.setup(width=1920, height=1080)
window.tracer(0)

# Paddle Left
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("White")
paddle_left.shapesize(stretch_wid=10, stretch_len=2)
paddle_left.penup()
paddle_left.goto(-800, 0)

# Paddle Right
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("White")
paddle_right.shapesize(stretch_wid=10, stretch_len=2)
paddle_right.penup()
paddle_right.goto(800, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)


# Functions
def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)


def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)


def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)


def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)


# Keyboard binding
window.listen()
window.onkeypress(paddle_left_up, "w")
window.onkeypress(paddle_left_down, "s")
window.onkeypress(paddle_right_up, "Up")
window.onkeypress(paddle_right_down, "Down")

# main game loop
while True:
    window.update()
