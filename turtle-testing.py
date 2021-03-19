import turtle

# following Keith Galli's Youtube tutorial

bob = turtle.Turtle()
bob.color("steelblue", "green") # outline, fill

bob.begin_fill()
for x in range(4):
    bob.forward(100)
    bob.right(90)
bob.end_fill()

bob.penup()
bob.forward(150)
bob.pendown()

bob.color("orange", "red") # outline, fill
bob.begin_fill()
for x in range(4):
    bob.forward(100)
    bob.right(90)
bob.end_fill()

bob.setheading(90) # turn north
bob.heading()

turtle.done() # keeps animation window open