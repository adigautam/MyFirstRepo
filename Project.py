from turtle import *
from random import randint
speed(20)
penup()
goto(-140,140)
for step in range(16):
    write(step,align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

for step in range(2):
    ada = Turtle()
    ada.color('red')
    ada.shape('turtle')

    ada.penup()
    ada.goto(-160,100)
    ada.right(360)
    ada.pendown()

    bob=Turtle()
    bob.color('blue')
    bob.shape('turtle')

    bob.penup()
    bob.goto(-160,70)
    bob.right(360)
    bob.pendown()

    for turn in range(160):
        ada.forward(randint(1,3))
        bob.forward(randint(1,3))

       
