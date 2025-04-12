import turtle
import random
import math

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create and configure the screen
screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("white")
screen.title("Turtle Game")

class MovingTurtle(turtle.Turtle):
    def __init__(self, shape='turtle', size=1, color='black'):
        super().__init__()
        self.shape(shape)
        self.shapesize(size)
        self.color(color)
        self.penup()
        self.speed(0)  # Set speed to maximum, we control movement manually

    def move_forward(self, distance):
        self.forward(distance)
        self.color(random.choice(['red', 'orange', 'green', 'blue', 'purple']))
        self.check_borders()

    def move_backward(self, distance):
        self.backward(distance)
        self.color(random.choice(['red', 'orange', 'green', 'blue', 'purple']))
        self.check_borders()

    def turn_left(self):
        self.left(90)

    def turn_right(self):
        self.right(90)

    def distance_to(self, other):
        return self.distance(other)

    def check_borders(self):
        # Get the current position of the turtle
        x, y = self.position()
        # Define borders
        x_limit = SCREEN_WIDTH / 2 - 50
        y_limit = SCREEN_HEIGHT / 2 - 50

        # Check if the turtle is out of bounds and correct its position
        if x > x_limit:
            x = x_limit
        elif x < -x_limit:
            x = -x_limit
        if y > y_limit:
            y = y_limit
        elif y < -y_limit:
            y = -y_limit

        self.goto(x, y)

class MotherTurtle(MovingTurtle):
    def __init__(self):
        super().__init__(size=5, color='red')

class FollowerTurtle(MovingTurtle):
    def __init__(self):
        super().__init__(size=2, color=random.choice(['blue', 'green', 'orange', 'purple']))
        self.follow_speed = 9  # Adjust the speed of followers

    def follow(self, mother, follow_distance):
        # Calculate the desired position
        angle = mother.heading()
        x, y = mother.position()
        x_offset = follow_distance * math.cos(math.radians(angle + 180))
        y_offset = follow_distance * math.sin(math.radians(angle + 180))
        target_x = x + x_offset
        target_y = y + y_offset

        # Move towards the target position gradually
        current_x, current_y = self.position()
        direction = math.atan2(target_y - current_y, target_x - current_x)
        distance_to_move = self.follow_speed
        if self.distance_to(mother) > follow_distance:
            self.setheading(math.degrees(direction))
            self.forward(distance_to_move)
        self.check_borders()

class TurtleController:
    def __init__(self):
        self.mother = MotherTurtle()
        self.followers = [FollowerTurtle() for _ in range(5)]
        self.setup_controls()
        self.position_followers()
        self.update_followers()
    
    def setup_controls(self):
        turtle.listen()
        turtle.onkey(lambda: self.mother.move_forward(50), 'Up')
        turtle.onkey(lambda: self.mother.move_backward(50), 'Down')
        turtle.onkey(self.mother.turn_left, 'Left')
        turtle.onkey(self.mother.turn_right, 'Right')
    
    def position_followers(self):
        # Place each follower turtle at a random distance and angle from the mother turtle
        for follower in self.followers:
            distance = random.randint(150, 250)  # Random distance from the mother turtle
            angle = random.uniform(0, 360)  # Random angle
            x = distance * math.cos(math.radians(angle))
            y = distance * math.sin(math.radians(angle))
            follower.goto(self.mother.xcor() + x, self.mother.ycor() + y)
            follower.setheading(self.mother.heading())
    
    def update_followers(self):
        follow_distance = 100
        min_distance_between_followers = 30  # Minimum distance between followers

        for follower in self.followers:
            follower.follow(self.mother, follow_distance)

            # Ensure followers don't get too close to each other
            for other in self.followers:
                if follower != other and follower.distance_to(other) < min_distance_between_followers:
                    self.reposition_follower(follower, other)

        turtle.ontimer(self.update_followers, 100)

    def reposition_follower(self, follower, other):
        # Move the follower to a new position away from the other follower
        angle = random.uniform(0, 360)
        distance = 150  # Move to a distance away
        x = distance * math.cos(math.radians(angle))
        y = distance * math.sin(math.radians(angle))
        follower.goto(other.xcor() + x, other.ycor() + y)
        follower.setheading(other.heading())

# Create and start the TurtleController
TurtleController()

# Main loop
turtle.mainloop()
