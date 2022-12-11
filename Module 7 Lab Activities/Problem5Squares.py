# Edward Jimenez
# 11/28/22
# Write a program with the following chunk of code. Modify this code to produce the
# image shown on the right

import turtle


def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("blue")
alex.speed(100)

sz = 50
for i in range(6):
    draw_square(alex, sz)
    sz += 20
    alex.penup()
    alex.right(135)
    alex.forward(15)
    alex.left(135)
    alex.pendown()

wn.exitonclick()
