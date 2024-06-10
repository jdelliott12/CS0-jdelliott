import turtle

t = turtle.Turtle()

t.speed(1)

side_length = 20

turtle.bgcolor("lightgreen")

t.color("hotpink")

for i in range(4):
    t.penup()
    t.goto(-side_length / 2, side_length / 2)
    t.pendown()

    for _ in range(4):
        t.forward(side_length)
        t.right(90)

    side_length += 20

t.hideturtle()

turtle.done()