import turtle
tao = turtle.Pen()
tao.shape('turtle')

def circle():
    for i in range(20):
        tao.circle(70)
        tao.right(18)

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Go(-100,70)
circle()

