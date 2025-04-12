import turtle as neil
import random

# Set up the screen
neil.title("Paddle Game")
neil.bgcolor("black")
neil.setup(width=800, height=600)

# Create the paddles
def create_paddle(color, x_position):
    paddle = neil.Turtle()
    paddle.shape('square')
    paddle.penup()
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.color(color)
    paddle.goto(x_position, 0)
    return paddle

r1 = create_paddle('orange', 350)
r2 = create_paddle('blue', -350)

# Functions to move paddles
def move_paddle(paddle, dy):
    y = paddle.ycor()
    if -240 < y + dy < 250:  # Limit the paddle movement
        paddle.sety(y + dy)

def up():
    move_paddle(r1, 20)

def down():
    move_paddle(r1, -20)

def up2():
    move_paddle(r2, 20)

def down2():
    move_paddle(r2, -20)

# Set up keyboard controls
neil.listen()
neil.onkeypress(up, 'Up')
neil.onkeypress(down, 'Down')
neil.onkeypress(up2, 'w')
neil.onkeypress(down2, 's')

# Create the ball
ball = neil.Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.speed(0)
ball.goto(0, 0)
ball.dx = 2 * random.choice((1, -1))  # Randomly set initial direction
ball.dy = 2 * random.choice((1, -1))

# Move the ball
def move_ball():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bounce off the top and bottom edges
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Bounce off paddles
    if (340 < ball.xcor() < 350) and (r1.ycor() - 50 < ball.ycor() < r1.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
    elif (-350 < ball.xcor() < -340) and (r2.ycor() - 50 < ball.ycor() < r2.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1

    # Reset ball if it goes out of bounds
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= random.choice((1, -1))  # Randomly reset direction

    neil.ontimer(move_ball, 20)  # Continue moving the ball

# Start moving the ball
move_ball()

# Main loop
neil.mainloop()
