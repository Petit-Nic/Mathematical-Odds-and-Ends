from graphics import *

def drawTriangle(points, window, color):
    triangle = Polygon(points)
    triangle.setWidth(0)
    triangle.setFill(color)
    triangle.draw(window)

def getMid(points):
    x_coord = (points[0].getX()+points[1].getX())/2
    y_coord = (points[0].getY()+points[1].getY())/2
    return Point(x_coord, y_coord)

def sierpinski(points, level, color, window):
    drawTriangle(points, window, color)
    leftmid = getMid([points[0], points[1]])
    botmid = getMid([points[0], points[2]])
    rightmid = getMid([points[1], points[2]])
    drawTriangle([leftmid, rightmid, botmid], window, 'white')
    if level > 0:
       # sierpinski([points[0], leftmid, botmid], level - 1, color, window)
        sierpinski([leftmid, points[1], rightmid], level - 1, color, window)
       # sierpinski([botmid, rightmid, points[2]], level - 1, color, window)

def main():
    #get the depth from the system arguments
    depth = 3
    #set up the window using GraphWin
    window = GraphWin('Sierpinski Triangle', 1000, 866)
    #set the coordinates of the window
    window.setCoords(-201, -101, 201, 251)
    #list the starting points for the first square
    points = [Point(-200,-100), Point(0,250), Point(200,-100)]

    #call the function with the points
    sierpinski(points, depth, 'pink', window)
    #close the window when clicked
    window.getMouse()
    window.postscript(file = "sierp3.eps")
    window.close()

main()
