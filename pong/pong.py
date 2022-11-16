import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("pink") #colors - https://matplotlib.org/3.1.0/gallery/color/named_colors.html
wn.setup(width=800, height=600)
wn.tracer(0)
# score
score_pa = 0
score_pb = 0




#Paddle1
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


#Paddle2
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize()
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2
# ball.dx = .5/5
# ball.dy = .5/5

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  \nPlayer B: 0", align="center", font=("Veranda", 24, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keybinding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()
    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # borders
    if ball.ycor() > 290: #top border
        ball.sety(290)
        ball.dy *= -1
        # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290: #bottom border
        ball.sety(-290)
        ball.dy *= -1
        # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() > 390: #right border
        ball.goto(0, 0)
        ball.dx*= -1
        score_pa += 1
        pen.clear()
        pen.write("Player A: {}  \nPlayer B: {}".format(score_pa, score_pb), align="center", font=("Veranda", 24, "normal"))
        # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() < -390: #left
        ball.goto(0, 0)
        ball.dx*= -1
        score_pb += 1
        pen.clear()
        pen.write("Player A: {}  \nPlayer B: {}".format(score_pa, score_pb), align="center", font=("Veranda", 24, "normal"))
        # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    # paddle hit
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1