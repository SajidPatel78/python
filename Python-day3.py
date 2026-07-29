from turtle import *
import turtle

# Background color
turtle.bgcolor("black")

# Pen and fill colors
color("orange", "yellow")

begin_fill()

while True:
    forward(200)
    left(170)

    # Stop when turtle returns near the starting point
    if distance(0, 0) < 1:
        break

end_fill()

done()