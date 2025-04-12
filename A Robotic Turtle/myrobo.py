import turtle
import random
import math

class MovingTurtle(turtle.Turtle):
    def __init__(self, shape='turtle', size=1, color='black'):
        super().__init__()
        self.shape(shape)
        self.shapesize(size)
        self.color(color)
        self.penup()
    
    def move_forward(self, distance):
        self.forward(distance)
        self.color(random.choice(['red', 'orange', 'green', 'blue', 'purple']))

    def move_backward(self, distance):
        self.backward(distance)
        self.color(random.choice(['red', 'orange', 'green', 'blue', 'purple']))
    
    def turn_left(self):
        self.left(90)

    def turn_right(self):
        self.right(90)

class MotherTurtle(MovingTurtle):
    def __init__(self):
        super().__init__(size=10, color='red')

class FollowerTurtle(MovingTurtle):
    def __init__(self):
        super().__init__(size=5, color=random.choice(['blue', 'green', 'orange', 'purple']))
    
    def follow(self, mother, distance):
        angle = mother.heading()
        x, y = mother.position()
        x_offset = distance * math.cos(math.radians(angle + 180))
        y_offset = distance * math.sin(math.radians(angle + 180))
        self.setheading(angle)
        self.goto(x + x_offset, y + y_offset)

class TurtleController:
    def __init__(self):
        self.mother = MotherTurtle()
        self.followers = [FollowerTurtle() for _ in range(5)]
        self.setup_controls()
        self.update_followers()
    
    def setup_controls(self):
        turtle.listen()
        turtle.onkey(lambda: self.mother.move_forward(50), 'Up')
        turtle.onkey(lambda: self.mother.move_backward(50), 'Down')
        turtle.onkey(self.mother.turn_left, 'Left')
        turtle.onkey(self.mother.turn_right, 'Right')
    
    def update_followers(self):
        for follower in self.followers:
            follower.follow(self.mother, 100)
        turtle.ontimer(self.update_followers, 100)

# Create and start the TurtleController
TurtleController()

# Main loop
turtle.mainloop()
