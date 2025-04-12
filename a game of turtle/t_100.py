import turtle as t

n = t.Turtle()
n.forward(400)
n.left(90)
n.speed('fastest')
n.color('blue')
# loop to make multiple circles
for i in range(0,500,2):
    n.circle(i+10)

n.right(90)
n.color('red')
n.backward(400)
n.left(90)

# loop to make multiple circles
for i in range(500,0,-2):
    n.circle(i+10)


t.mainloop()


