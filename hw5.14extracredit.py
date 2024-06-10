import turtle

def draw_bar(t, height):
    if height >= 200:
        t.fillcolor('red')
    elif height >= 100:
        t.fillcolor('yellow')
    else:
        t.fillcolor('green')


    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.forward(10)


wn = turtle.Screen()

wn.bgcolor("white")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(2)

xs = [22,101,125,88,212,260,195,201,44,118] 
for a in xs:
    draw_bar(tess, a)


wn.mainloop()