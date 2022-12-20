import turtle
import os


class Ball(object):
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape('square')
        self.ball.color('white')
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 2
        self.ball.dy = 2

    def ball_movement(self):
        self.ball.dx = self.ball.dx
        self.ball.dy = self.ball.dy
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)
        return self.ball

