import turtle
import os


def window_creation():
    wn = turtle.Screen()
    wn.title('Pong')
    wn.bgcolor('black')
    wn.setup(width=800, height=600)
    wn.tracer(0)
    return wn


def redraw_function(surface):
    surface.update()

