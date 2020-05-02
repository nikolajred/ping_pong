import turtle
from random import choice, randint

window = turtle.Screen()
window.title("Pin-pong")
window.setup(width=1.0, height=1.0)
window.bgcolor("black")
border = turtle.Turtle()
border.color("gray")
border.speed(0)
border.begin_fill()
border.goto(-500, 300)
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()

border.goto(0, 300)
border.color("red")
border.setheading(270)
for i in range(25):
    if i % 2 == 0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.hideturtle()

rocket_a = turtle.Turtle()
rocket_a.speed(3)
rocket_a.shape("square")
rocket_a.color("white")
rocket_a.shapesize(stretch_wid=5, stretch_len=1)
rocket_a.penup()
rocket_a.goto(-450, 0)


def move_up_a():
    y = rocket_a.ycor() + 10
    if y > 250:
        y = 250
    rocket_a.sety(y)


def move_down_a():
    y = rocket_a.ycor() - 10
    if y < -250:
        y = -250
    rocket_a.sety(y)


rocket_b = turtle.Turtle()
rocket_b.speed(3)
rocket_b.shape('square')
rocket_b.color('white')
rocket_b.shapesize(stretch_wid=5, stretch_len=1)
rocket_b.penup()
rocket_b.goto(450, 0)

FONT = ("TimesNewRoman", 52)
score_a = 0
score_1 = turtle.Turtle(visible=False)
score_1.color('white')
score_1.penup()
score_1.setposition(-200, 300)
score_1.write(score_a, font=FONT)

score_b = 0
score_2 = turtle.Turtle(visible=False)
score_2.color('white')
score_2.penup()
score_2.setposition(200, 300)
score_2.write(score_b, font=FONT)

def move_up_b():
    y = rocket_b.ycor() + 10
    if y > 250:
        y = 250
    rocket_b.sety(y)


def move_down_b():
    y = rocket_b.ycor() - 10
    if y < -250:
        y = -250
    rocket_b.sety(y)


ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.speed(3)
ball.dx = 3
ball.dy = -3
ball.penup()

window.listen()
window.onkeypress(move_up_a, "w")
window.onkeypress(move_down_a, "s")
window.onkeypress(move_up_b, "Up")
window.onkeypress(move_down_b, "Down")

while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:
        ball.dy = -ball.dy

    if ball.ycor() <= -290:
        ball.dy = -ball.dy

    if ball.xcor() >= 490:
        score_b += 1
        score_2.clear()
        score_2.write(score_b, font=FONT)
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

    if ball.xcor() <= -490:
        score_a += 1
        score_1.clear()
        score_1.write(score_a, font=FONT)
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

    if rocket_b.ycor() - 50 <= ball.ycor() <= rocket_b.ycor() + 50 \
            and rocket_b.xcor() - 5 <= ball.xcor() <= rocket_b.xcor() + 5:
        ball.dx = -ball.dx

    if rocket_a.ycor() - 50 <= ball.ycor() <= rocket_a.ycor() + 50 \
            and rocket_a.xcor() - 5 <= ball.xcor() <= rocket_a.xcor() + 5:
        ball.dx = -ball.dx

window.mainloop()
