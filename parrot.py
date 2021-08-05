# Parrot in pixels

import turtle

parrot = turtle.Turtle()
side = 10
parrot.width(1)
numSquares = 18




def drawSquare(color):
    parrot.color(color)
    parrot.begin_fill()
    for i in range(4):
        parrot.forward(side)
        parrot.right(90)
    parrot.end_fill()
    parrot.forward(side)

def nextRow():
    parrot.penup()
    parrot.backward(numSquares * side)
    parrot.left(90)
    parrot.forward(side)
    parrot.right(90)
    parrot.pendown()

def drawRow(colors, numbers):
    for j in range(len(colors)):
        for k in range(numbers[j]):
            drawSquare(colors[j])
    nextRow()


colorpalett = ["black", "white", "#65fe08", "#4ac300", "#206F19"]

#line 1
colors = ["white", "black", "white", "black", "white", "#4ac300", "white"]
numbers = [3, 2, 3, 2, 2, 3, 3]
drawRow(colors, numbers)

#line 2
colors = ["white", "black", "white", "black", "white", "#4ac300", "white"]
numbers = [3, 2, 3, 2, 1, 3, 4]
drawRow(colors, numbers)

#line 3
colors = ["white", "black", "white", "black", "white", "#4ac300", "white", "#65fe08", "#206F19"]
numbers = [4, 2, 1, 2, 1, 3, 2, 2, 1]
drawRow(colors, numbers)

#line4
colors = ["white", "black", "white", "black", "white", "#4ac300", "white", "#65fe08", "#206F19"]
numbers = [4, 2, 1, 2, 1, 3, 2, 1, 2]
drawRow(colors, numbers)

#line 5
colors = ["white", "#4ac300", "#65fe08", "white"]
numbers = [4, 8, 4, 2]
drawRow(colors, numbers)

#line 6
colors = ["white", "#4ac300", "#65fe08", "#206F19", "white"]
numbers = [2, 9, 2, 3, 2]
drawRow(colors, numbers)

#line 7
colors = ["white", "#4ac300", "#65fe08", "#206F19", "white"]
numbers = [2, 8, 2, 4, 2]
drawRow(colors, numbers)

#line 8
colors = ["white", "#4ac300", "#65fe08", "#206F19", "white"]
numbers = [2, 6, 3, 5, 2]
drawRow(colors, numbers)

#line 9
colors = ["white", "#4ac300", "#65fe08", "#206F19", "white"]
numbers = [2, 5, 2, 6, 3]
drawRow(colors, numbers)

#line 10
colors = ["white", "#4ac300", "#65fe08", "#206F19", "white"]
numbers = [2, 5, 1, 7, 3]
drawRow(colors, numbers)

#line 11
colors = ["white", "#4ac300", "#65fe08", "#206F19", "white"]
numbers = [2, 4, 2, 7, 3]
drawRow(colors, numbers)

#line 12
colors = ["white", "#4ac300", "#65fe08", "#206F19", "white"]
numbers = [2, 4, 1, 8, 3]
drawRow(colors, numbers)

#line 13
colors = ["white", "#4ac300", "#65fe08", "#206F19", "white"]
numbers = [2, 5, 1, 5, 5]
drawRow(colors, numbers)

#line 14
colors = ["white", "#4ac300", "#65fe08", "#206F19", "white"]
numbers = [3, 4, 1, 5, 5]
drawRow(colors, numbers)

#line 15
colors = ["white", "#4ac300", "white"]
numbers = [5, 7, 6]
drawRow(colors, numbers)

#line 16
colors = ["white", "black", "white", "#4ac300", "white"]
numbers = [1, 1, 3, 7, 6]
drawRow(colors, numbers)

#line 17 ???
colors = ["white", "black", "#4ac300", "white"]
numbers = [1, 5, 5, 7]
drawRow(colors, numbers)

#line 18
colors = ["white", "black", "#4ac300", "white", "#4ac300", "white"]
numbers = [1, 5, 1, 2, 2, 7]
drawRow(colors, numbers)

#line 19
colors = ["white", "black", "#4ac300", "black", "white", "#4ac300", "white"]
numbers = [3, 3, 1, 1, 1, 2, 7]
drawRow(colors, numbers)

#line 20
colors = ["white", "black", "#4ac300", "white"]
numbers = [3, 3, 5, 7]
drawRow(colors, numbers)

#line 21
colors = ["white", "#4ac300", "white"]
numbers = [6, 3, 9]
drawRow(colors, numbers)

#line 22
colors = ["white", "#4ac300", "white"]
numbers = [6, 3, 9]
drawRow(colors, numbers)
