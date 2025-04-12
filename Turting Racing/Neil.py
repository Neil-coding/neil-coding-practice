import turtle
import random

Neil = turtle.Turtle()
Neil.color('blue')
Neil.shape('turtle')
Neil.shapesize(8,8)
Neil.penup()

umair = turtle.Turtle()
umair.color('green')
umair.shape('turtle')
umair.shapesize(8,8)
umair.penup()


Neil.goto(-400,200)
umair.goto(-400,-200)


for i in range(50):
    Neil.forward(random.randint(1,20))
    umair.forward( random.randint(1,20) )


if Neil.xcor()>umair.xcor():
    turtle.write('Neil Won')
    umair.hideturtle()
else:
    turtle.write('Umair Won')
    Neil.hideturtle()

# next time contraol this game with keybord!


turtle.mainloop()
