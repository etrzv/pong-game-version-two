import turtle
import os
from window_settings import window_creation, redraw_function
from ball_settings import Ball
from paddles import *
from borders import *


def main():
    window_creation()
    window = window_creation()
    ball = Ball()

    while True:
        redraw_function(window)
        ball.ball_movement()
        movement_check(window)
        border_score_function(ball, window)


if __name__ == '__main__':
    main()
