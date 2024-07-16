from PIL import Image as NewImage
from graphics import *

def drawSquare(points, window, color):
    #points is a list of the top left coordinate followed by bottom right coordinate
    #squares are drawn without borders
    square = Rectangle(points[0], points[1])
    square.setWidth(0)
    square.setFill(color)
    square.draw(window)

def sierpinskiCarpet(points, level, window, color, n):
    #n is the number of subrectangles per side, color is the color of the drawn parts;
    #upon first call points is a list of the top left coordinate followed by bottom right
    #coordinate, both expressed as Point(x,y); level is the number of recursions desired

    if level == 0:
        drawSquare(points, window, color)
    else:
        x_coords = [points[0].getX()]
        stepX = (points[1].getX()-points[0].getX())/n
        for i in range(n):
            x_coords.append(points[0].getX() + (i+1)*stepX)

        y_coords = [points[1].getY()]
        stepY = (points[0].getY()-points[1].getY())/n
        for i in range(n):
            y_coords.append(points[1].getY() + (i+1)*stepY)

        for i in range(n):
            for j in range(n):
                #creating fully black squares
                if (i == 2 and (j == 2 or j==0)):
                    drawSquare([Point(x_coords[j], y_coords[i+1]), Point(x_coords[j+1], y_coords[i])], window, color)
                else:
                    if (i > 1 or j > 2) : #selecting squares that are self-similar
                      sierpinskiCarpet([Point(x_coords[j], y_coords[i+1]), Point(x_coords[j+1], y_coords[i])],
                             level - 1, window, color, n)



# sierpinskiCarpet(SQUARE, level - 1, window, color) to draw repeating pattern
#  drawSquare(SQUARE, window, color) to draw solid square
# Comment out sierpinskiCarpet to draw white repeating square




def main():
    depth = 4
    subdivisions = 5
    size = subdivisions ** depth
    margin = size // 20
    #set up the window using GraphWin
    window = GraphWin('Sierpinski Carpet', 1000+2*margin, 1000+2*margin)
    #list the starting points for the first square
    points = [Point(0, size), Point(size, 0)]
    #set the coordinates of the window
    window.setCoords(-margin, -margin, size+margin, size+margin)


    #call the function with the points
    sierpinskiCarpet(points, depth, window, 'purple', subdivisions)
    #close the window when clicked
    window.getMouse()
    window.postscript(file = "sierp.eps")
    window.close()

    img = NewImage.open("sierp.eps")
    img.save("sierp.png", "png")

main()
