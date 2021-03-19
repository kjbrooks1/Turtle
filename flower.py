import turtle

# following Keith Galli's Youtube tutorial

sophie = turtle.Turtle()
sophie.color("red", "pink") # outline, fill
sophie.speed(10)

sophie.begin_fill()
for x in range(9):
    sophie.forward(200)
    sophie.left(160)
    sophie.forward(200)
sophie.end_fill()



turtle.done()