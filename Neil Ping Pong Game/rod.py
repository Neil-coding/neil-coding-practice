import turtle as neil 

r1 = neil.Turtle()
r1.shape('square')
r1.penup()
r1.shapesize(1,5)
r1.color('orange')
r1.left(90)
r1.goto(400,0)



r2 = neil.Turtle()
r2.shape('square')
r2.penup()
r2.shapesize(1,5)
r2.left(90)
r2.color('blue')
r2.goto(-400,0)


def up():
    r1.forward(50)
def down():
    r1.forward(-50)

neil.listen()

neil.onkeypress(up,'Up')
neil.onkeypress(down,'Down')

def up2():
    r2.forward(50)
def down2():
    r2.forward(-50)

neil.onkeypress(up2,'w')
neil.onkeypress(down2,'s')




ball = neil.Turtle()
ball.shape('circle')
ball.color('blue')


neil.mainloop()
