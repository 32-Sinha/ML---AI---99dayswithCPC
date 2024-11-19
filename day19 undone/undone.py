import turtle

def hilbert_curve(t, order, size, parity):
    if order == 0:
        return

    t.right(parity * 90)
    hilbert_curve(t, order - 1, size, -parity)
    t.forward(size)
    t.left(parity * 90)
    hilbert_curve(t, order - 1, size, parity)
    t.forward(size)
    hilbert_curve(t, order - 1, size, parity)
    t.left(parity * 90)
    t.forward(size)
    hilbert_curve(t, order - 1, size, -parity)
    t.right(parity * 90)

# Set up the turtle
turtle.speed(0)
turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()

# Draw the Hilbert Curve
order = 4
size = 10
hilbert_curve(turtle, order, size, 1)

# Hide the turtle and display the window
turtle.hideturtle()
turtle.done()
