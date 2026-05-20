import turtle
import random

turtle.colormode(255)

t = turtle.Turtle()
t.speed("fastest")
t.penup()
t.hideturtle()

color_list = [
    (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135),
    (52, 93, 124), (172, 154, 99), (140, 30, 19), (133, 163, 185),
    (198, 91, 71), (46, 122, 86), (72, 43, 35), (157, 196, 169),
    (55, 46, 50), (103, 148, 138), (179, 95, 93), (134, 83, 107),
    (18, 86, 90), (82, 148, 129), (147, 17, 19), (27, 68, 102),
    (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102),
]

t.setheading(225)
t.forward(300)
t.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen = turtle.Screen()
screen.exitonclick()