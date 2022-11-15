import math  
import turtle
import time
def Translate(X,Y,angle,distance):                #defines function
    # 0 degrees = North, 90 = East, 180 = South, 270 = West
    dY = distance*math.cos(math.radians(angle))   #change in y 
    dX = distance*math.sin(math.radians(angle))   #change in x 
    Xfinal = X + dX                               
    Yfinal = Y + dY
    return Xfinal, Yfinal
turtle.screensize(10, 10)
t = turtle.Turtle()
t.left(90)

t.forward(400)
t.backward(790)
x, y = Translate(0, 0, 4, 36.168)
print(x, y)

t.goto(x,y)

time.sleep(1)