import turtle
import time

turtle.screensize(10, 10)
t = turtle.Turtle()
t.left(90)

t.forward(400)
t.backward(790)
x, y = t.xcor, t.ycor
print(x)
print(y)
t.goto(0,0)

time.sleep(1)