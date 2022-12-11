# Edward Jimenez
# 11/1/22

# Uses the turtle module to create a drawing based on the user's input

import turtle

TT = turtle.Turtle()
screen = turtle.Screen()

side_length = int(input("What is the side length? "))
fill_color = input("What is the fill color? ")
shape = input("What shape would you like to draw, triangle or square? ")

TT.pencolor(fill_color)
TT.color(fill_color)
TT.fillcolor(fill_color)
TT.begin_fill()
TT.speed(10000)

if shape == "triangle":
    for num in range(3):
        TT.forward(side_length)
        TT.right(120)

elif shape == "square":
    for num in range(4):
        TT.forward(side_length)
        TT.right(90)

TT.end_fill()
screen.exitonclick()
