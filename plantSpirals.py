from PIL import Image as NewImage
import math, numpy
import turtle

def drawPhyllotacticPattern( t,  density = 137.508, cspread = 4, petalstart = False, ):
        """print a pattern of circles using spiral phyllotactic data"""
        # initialize position
        turtle.pen(outline=1, pencolor="blue", fillcolor="orange")
        turtle.hideturtle()
        # turtle.color("orange")
        phi = 360/density * ( math.pi / 180.0 )
        xcenter = 0.0
        ycenter = 0.0

        # for loops iterate in this case from the first value until < 4, so
        for n in range (0, t):
                r = cspread * math.sqrt(n)
                theta = n * phi

                x = r * math.cos(theta) + xcenter
                y = r * math.sin(theta) + ycenter

                # move the turtle to that position and draw
                turtle.up()
                turtle.setpos(x, y)
                turtle.down()
                # orient the turtle correctly
                turtle.setheading(n * 360/density)
                if petalstart:
                        #turtle.color("yellow")
                        drawPetal(x, y)
                else: turtle.circle(5, steps=180)

        turtle.up()


def drawPetal( x, y ):
        turtle.up()
        turtle.setpos(x, y)
        turtle.down()
        turtle.begin_fill()
        #turtle.fill(True)
        turtle.pen(outline=1, pencolor="black", fillcolor="yellow")
        turtle.right(20)
        turtle.forward(100)
        turtle.left(40)
        turtle.forward(100)
        turtle.left(140)
        turtle.forward(100)
        turtle.left(40)
        turtle.forward(100)
        turtle.up()
        turtle.end_fill() # this is needed to complete the last petal



print("What value of d do you wish to use? Input d as (a+sqrt(b))/c, where a,b can be 0 and c can be 1")
a = int(input('Value of a: '))
b = int(input('Value of b: '))
c = int(input('Value of c: '))
print("How many seeds should the picture have?")
det = int(input("Enter 1 for a few, 2 for more, 3 for the most: "))
turtle.shape("turtle")
turtle.speed(0) # make the turtle go as fast as possible
drawPhyllotacticPattern( 400*det, (a+b**(1/2))/c, 10 )
cv = turtle.getcanvas()
cv.postscript(file="plantSpiral.ps", colormode='color')
turtle.bye() # lets you x out of the window when outside of idle

img = NewImage.open("plantSpiral.ps")
img.save("plantSpiral.png", "png")
