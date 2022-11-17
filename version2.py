import math  
import turtle

t = turtle.Turtle()
t.left(90)
t.forward(400)
t.backward(790)
t.goto(0, 0)
X = 0
Y = 0
angle = 0
distance = 0

while True:
    def Translate(X,Y,angle,distance):                #defines function
        # 0 degrees = North, 90 = East, 180 = South, 270 = West
        dY = distance*math.sin(math.radians(angle))   #change in y 
        dX = distance*math.cos(math.radians(angle))   #change in x 
        Xfinal = X + dX                               
        Yfinal = Y + dY
        return Xfinal, Yfinal
	@@ -27,4 +27,4 @@ def Translate(X,Y,angle,distance):                #defines function
    X, Y = t.pos()
    print(X, Y)
    angle = int(input("angle:"))
    distance = int(input("distance:"))
