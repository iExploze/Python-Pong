import turtle

window = turtle.Screen()
window.title("Pong for learning")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle Left
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("White")
paddle_left.penup()
paddle_left.goto(-350, 0)


# Paddle Right


# Ball


# main game loop
while True:
    window.update()
