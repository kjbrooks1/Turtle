import turtle

# following Keith Galli's Youtube tutorial

ET = turtle.Turtle()
turtle.bgcolor("steelblue")
ET.speed(20)

# move so that star is in center of page
ET.penup()
ET.backward(100)
ET.pendown()

def star(turtle, size):
    if( size <= 10):
        return 0
    for x in range(5):
        turtle.forward(size)
        star(turtle, size/4)
        turtle.left(216)
    

star(ET, 200)

turtle.done()