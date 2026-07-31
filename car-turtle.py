from turtle import *

speed(0)
bgcolor("skyblue")
pensize(3)

# -----------------------------
# Sun
# -----------------------------
penup()
goto(250, 180)
pendown()
color("yellow")
begin_fill()
circle(40)
end_fill()

# -----------------------------
# Clouds
# -----------------------------
def cloud(x, y):
    penup()
    goto(x, y)
    pendown()
    color("white")
    begin_fill()
    circle(20)
    penup()
    goto(x+20, y+10)
    pendown()
    circle(25)
    penup()
    goto(x+45, y)
    pendown()
    circle(20)
    end_fill()

cloud(-250,180)
cloud(-50,150)

# -----------------------------
# Road
# -----------------------------
penup()
goto(-400,-120)
pendown()
color("gray")
begin_fill()

goto(400,-120)
goto(400,-300)
goto(-400,-300)
goto(-400,-120)

end_fill()

# Road markings
color("white")
pensize(5)

for x in range(-350,351,80):
    penup()
    goto(x,-210)
    pendown()
    forward(40)

pensize(3)

# -----------------------------
# Car Body
# -----------------------------
penup()
goto(-180,-70)
pendown()

color("royalblue")
begin_fill()

forward(300)
left(90)
forward(60)

right(45)
forward(60)

right(45)
forward(100)

right(45)
forward(60)

right(45)
forward(60)

end_fill()

# -----------------------------
# Windows
# -----------------------------
color("lightblue")

penup()
goto(-50,40)
pendown()

begin_fill()

left(135)
forward(70)
right(90)
forward(40)
right(90)
forward(70)
right(90)
forward(40)

end_fill()

penup()
goto(40,40)
pendown()

begin_fill()

forward(70)
right(90)
forward(40)
right(90)
forward(70)
right(90)
forward(40)

end_fill()

# -----------------------------
# Door
# -----------------------------
color("black")

penup()
goto(20,-10)
pendown()

setheading(270)

forward(70)
left(90)
forward(60)
left(90)
forward(70)

penup()
goto(70,-40)
dot(8)

# -----------------------------
# Wheels
# -----------------------------
def wheel(x,y):
    penup()
    goto(x,y)
    pendown()

    color("black")
    begin_fill()
    circle(30)
    end_fill()

    penup()
    goto(x+10,y+10)
    pendown()

    color("gray")
    begin_fill()
    circle(20)
    end_fill()

wheel(-120,-120)
wheel(120,-120)

# -----------------------------
# Headlight
# -----------------------------
penup()
goto(120,-10)
pendown()

color("yellow")
begin_fill()
circle(10)
end_fill()

# -----------------------------
# Tail Light
# -----------------------------
penup()
goto(-180,-10)
pendown()

color("red")
begin_fill()
circle(10)
end_fill()

# -----------------------------
# Ground
# -----------------------------
penup()
goto(-400,-120)
pendown()

color("green")
begin_fill()

goto(400,-120)
goto(400,-100)
goto(-400,-100)
goto(-400,-120)

end_fill()

hideturtle()
done()