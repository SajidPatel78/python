from turtle import *

speed(0)
bgcolor("white")
pensize(3)

# Head
penup()
goto(0, -180)
pendown()
color("blue")
begin_fill()
circle(180)
end_fill()

# Face
penup()
goto(0, -150)
pendown()
color("white")
begin_fill()
circle(150)
end_fill()

# Eyes
penup()
goto(-35, 80)
pendown()
color("white")
begin_fill()
circle(35)
end_fill()

penup()
goto(35, 80)
pendown()
begin_fill()
circle(35)
end_fill()

# Pupils
penup()
goto(-15, 95)
pendown()
color("black")
begin_fill()
circle(8)
end_fill()

penup()
goto(15, 95)
pendown()
begin_fill()
circle(8)
end_fill()

# Nose
penup()
goto(0, 40)
pendown()
color("red")
begin_fill()
circle(18)
end_fill()

# Nose line
penup()
goto(0, 40)
pendown()
color("black")
right(90)
forward(90)
left(90)

# Mouth
penup()
goto(-70, -50)
pendown()
circle(70, 180)

# Whiskers
penup()
goto(-30, 10)
pendown()
goto(-120, 30)

penup()
goto(-30, -10)
pendown()
goto(-120, -10)

penup()
goto(-30, -30)
pendown()
goto(-120, -50)

penup()
goto(30, 10)
pendown()
goto(120, 30)

penup()
goto(30, -10)
pendown()
goto(120, -10)

penup()
goto(30, -30)
pendown()
goto(120, -50)

hideturtle()
done()
