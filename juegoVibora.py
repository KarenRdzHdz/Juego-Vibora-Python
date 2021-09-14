"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.

Integrantes:
Karen Lizette Rodríguez Hernández - A01197734
Jorge Eduardo Arias Arias - A01570549
Hernán Salinas Ibarra - A01570409

14/09/2021

Ejercicios denotados por ***ejercicio realizado***

"""

from random import randrange
from turtle import *
import random

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
s = 100

#Shuffle and set colors
colors = ['blue','green', 'yellow', 'purple', 'black']
random.shuffle(colors)


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def changeSpeed(sp):
    global s 
    s = sp

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    "Food random without exiting boundaries"
    new_food_position_x = randrange(-1,1) * 10
    new_food_position_y = randrange(-1,1) * 10
    "Check if food will leave boundaries"
    if (new_food_position_x == -10) and (-140 < food.x):
        food.x = food.x + new_food_position_x
    if (new_food_position_x == 10) and (food.x < 140):
        food.x = food.x + new_food_position_x
    if (new_food_position_y == -10) and (-140 < food.y):
        food.y = food.y + new_food_position_y
    if (new_food_position_y == 10) and (food.y < 140):
        food.y = food.y + new_food_position_y


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    if not inside(head):
        if head.x < -200:
            head.x = 190
        if head.x > 190:
            head.x = -200
        if head.y < -200:
            head.y = 190
        if head.y > 190:
            head.y = -200
        update()

    snake.append(head)
    
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        #Assign color
        square(body.x, body.y, 9, colors[1])

    square(food.x, food.y, 9, colors[0])
    update()
    ontimer(move, s)

def clickLeft(x, y):
    change(-10, 0)

def clickRight(x, y):
    change(10, 0)

def clickMiddle(x, y):
    change(0, 10)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: changeSpeed(200), 'q')
onkey(lambda: changeSpeed(100), 'w')
onkey(lambda: changeSpeed(50), 'e')
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

onscreenclick(clickLeft, btn=1)
onscreenclick(clickRight, btn=3)
onscreenclick(clickMiddle, btn=2)

move()
print(snake)
done()