import turtle
import math
import random

# following Keith Galli's Youtube tutorial

pi = turtle.Turtle()
pi.color("brown")
pi.speed(12)

for i in range(100):
    pi.forward(math.sqrt(i)*i/2)
    pi.left(40)

pi.penup()
pi.goto(0,0)
pi.pendown()

pi.color("green")
for i in range(500):
    pi.forward(math.sqrt(i))
    pi.left(i%180)

pi.penup()
pi.goto(0,0)
pi.pendown()

pi.color("blue")
for i in range(500):
    pi.forward(40)
    pi.left(math.sin(i)*100)

pi.penup()
pi.goto(0,0)
pi.pendown()

pi.color("red")
for i in range(1000):
    pi.forward(random.randint(50,500))
    pi.left(random.randint(0,360))
    pi.right(random.randint(0,360))

turtle.done()