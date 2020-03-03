# Display triangle with another shaded smaller triangle inside of it.
# 2/27/2020
# CTI-110 P2HW2 - Turtle Graphic
# Koby Forbes
#
# Create a triangle
# Create smaller triangle within original triangle
# shade smaller triangle
#
import turtle
turtle.hideturtle()
turtle.goto(90, 180)
turtle.goto(180, 0)
turtle.goto(0, 0)
turtle.begin_fill()
turtle.goto(90, 60)
turtle.goto(180, 0)
turtle.end_fill()
