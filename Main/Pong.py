import turtle

window = turtle.Screen()
window.title("Pong for learning")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# main game loop
while True:
    window.update()
