"""
Doraemon drawing using Python Turtle graphics.
A simplified, stylized version built from basic shapes.

Run with: python doraemon_turtle.py
Requires: Python's built-in `turtle` module (no extra installs needed).
"""

import turtle

# ---------- Setup ----------
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("white")
screen.title("Doraemon - Turtle Graphics")

t = turtle.Turtle()
t.speed(0)          # fastest drawing speed
t.hideturtle()
t.width(3)


def goto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw_circle(x, y, radius, color, outline="black", start_fill=True):
    """Draw a filled circle with center roughly at (x, y)."""
    goto(x, y - radius)
    t.color(outline, color)
    if start_fill:
        t.begin_fill()
    t.circle(radius)
    if start_fill:
        t.end_fill()


def draw_oval(x, y, h_radius, v_radius, color, outline="black"):
    """Draw a filled oval (ellipse) centered roughly at (x, y)."""
    goto(x, y - v_radius)
    t.color(outline, color)
    t.begin_fill()
    for _ in range(2):
        t.circle(h_radius, 90)
        t.circle(v_radius, 90)
    t.end_fill()


# ---------- Head ----------
draw_circle(0, 150, 150, "#3AA9E0")          # blue head
draw_circle(0, 120, 110, "white")            # white face

# ---------- Ears ----------
draw_circle(-90, 260, 45, "white")
draw_circle(90, 260, 45, "white")
t.color("black")
t.pensize(3)
goto(-90, 300)
t.setheading(0)
t.forward(0)  # placeholder anchor
# small black outline circles already drawn via draw_circle outline

# ---------- Eyes ----------
draw_oval(-35, 195, 28, 35, "white")
draw_oval(35, 195, 28, 35, "white")
draw_circle(-25, 195, 7, "black")
draw_circle(25, 195, 7, "black")

# small white shine in the eyes
draw_circle(-22, 198, 2, "white")
draw_circle(28, 198, 2, "white")

# ---------- Nose ----------
draw_circle(0, 150, 18, "red")
draw_circle(3, 155, 4, "white")   # shine

# vertical line from nose to mouth
goto(0, 132)
t.setheading(270)
t.pendown()
t.color("black")
t.forward(60)
t.penup()

# ---------- Mouth ----------
goto(-90, 55)
t.setheading(0)
t.pendown()
t.pensize(3)
t.color("black")
t.circle(90, 180)  # mouth curve
t.penup()

# ---------- Whiskers ----------
for y in (170, 150, 130):
    goto(-40, y)
    t.setheading(200)
    t.pendown()
    t.forward(70)
    t.penup()

    goto(40, y)
    t.setheading(-20)
    t.pendown()
    t.forward(70)
    t.penup()

# ---------- Red collar & bell ----------
goto(-150, 0)
t.setheading(0)
t.pendown()
t.color("black", "red")
t.begin_fill()
t.forward(300)
t.circle(-150, 180)
t.forward(300)
t.circle(-150, 180)
t.end_fill()
t.penup()

draw_circle(0, -20, 22, "gold")
t.color("black")
goto(-20, -20)
t.pendown()
t.forward(40)
t.penup()
draw_circle(0, -10, 4, "black")

# ---------- Body ----------
goto(-160, -30)
t.setheading(0)
t.pendown()
t.color("black", "#3AA9E0")
t.begin_fill()
t.forward(320)
t.right(90)
t.circle(-320, 90)
t.forward(20)
t.circle(-40, 180)
t.forward(20)
t.circle(-320, 90)
t.end_fill()
t.penup()

# ---------- Belly pouch ----------
draw_oval(0, -130, 110, 70, "white")
goto(-110, -130)
t.setheading(0)
t.color("black")
t.pendown()
t.forward(220)
t.penup()

# ---------- Arms ----------
draw_circle(-200, -100, 35, "white")
draw_circle(200, -100, 35, "white")

# ---------- Feet ----------
draw_oval(-90, -320, 55, 30, "white")
draw_oval(90, -320, 55, 30, "white")

# ---------- Finish ----------
screen.update()
screen.exitonclick()  # click the window to close