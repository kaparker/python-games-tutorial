# Simple Pong in Python 3 for beginners
# Course by @TokyoEdTech
# Part 1: Getting Started

import turtle

wn = turtle.Screen()
wn.title("Pong By @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Main game loop
while True:
    wn.update()