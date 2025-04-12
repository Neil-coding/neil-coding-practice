import turtle
screen = turtle.Screen()

screen.register_shape('rocket.gif')

t1 = turtle.Turtle()
t1.shape('rocket.gif')

for i in range(360):
    t1.forward(1)
    t1.right(1)


t2 = turtle.Turtle()
t2.shape('turtle')

turtle.mainloop()