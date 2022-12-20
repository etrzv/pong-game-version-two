import turtle
import os
from ball_settings import *
from paddles import *
from window_settings import *


def border_score_function(ball, surface):
    ball = Ball.ball_movement(ball)
    score_a = 0
    score_b = 0
    score_board = turtle.Turtle()
    score_board.speed(0)
    score_board.color('white')
    score_board.penup()
    score_board.hideturtle()
    score_board.goto(0, 260)
    # score_board.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, 'normal'))

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system('afplay wall_hit.mp3&')

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system('afplay wall_hit.mp3&')

    elif ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_board.clear()
        score_a += 1
        # score_board.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, 'normal'))
        os.system('afplay point.mp3&')

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_board.clear()
        score_b += 1
        # score_board.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, 'normal'))
        os.system('afplay point.mp3&')

    elif (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1.03
        os.system('afplay paddle.mp3&')

    elif (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1.03
        os.system('afplay paddle.mp3&')

    if score_a == 5:
        score_board.write('Player A has won! Please click to leave.', align='center', font=('Courier', 24, 'normal'))
        surface.exitonclick()

    elif score_b == 5:
        score_board.write('Player B has won! Please click to leave.', align='center', font=('Courier', 24, 'normal'))
        surface.exitonclick()

