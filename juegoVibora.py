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

Exercises marked by ***ejercicio realizado***

"""
# Required libraries imported
from random import randrange
from turtle import *
import random

from freegames import square, vector

# Pre-stablished variables declared
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
#   Default speed stablished at 100
s = 100

#   Shuffle and set colors
colors = ['blue','green', 'yellow', 'purple', 'black']  # ***Exercise 5: change colors***
random.shuffle(colors)

# Function to change snake direction
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

# Function to change snake speed
def changeSpeed(sp):                                    # ***Exercise 1: changing the speed***                     
    global s 
    s = sp

# Function to check snake in boundaries
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

# Function to change food location
def move_food():                                        # ***Exercise 3: move the food***        
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

# Main movement function
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    
    if not inside(head):                                # ***Exercise 2: go around edges***        
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

# Functions to change direction with mouse clicks
def clickLeft(x, y):                                    # ***Exercise 4: respond to mouse clicks***
    change(-10, 0)

def clickRight(x, y):
    change(10, 0)

def clickMiddle(x, y):
    change(0, 10)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)

# Input detection
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

# Execution
move()
done()