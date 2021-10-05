from turtle import *
for angle in range(0, 360, 20):
    setheading(angle)
    forward(100)
    write(str(angle) + '*')
    backward(100)
