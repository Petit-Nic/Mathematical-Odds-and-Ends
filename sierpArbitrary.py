from graphics import *
from PIL import Image as NewImage

def drawTriangle(points, window, color):
    triangle = Polygon(points)
    triangle.setWidth(0)
    triangle.setFill(color)
    triangle.draw(window)

def subdivision(points, n):
    width = (points[2].getX()-points[0].getX())/n
    height = (points[1].getY()-points[0].getY())/n
    return [width, height]

def addwidth(point, width):
    xcoord = point.getX() + width
    return Point(xcoord, point.getY())

def addheight(point, height):
    ycoord = point.getY() + height
    return Point(point.getX(), ycoord)

def sierpinski(points, level, window, color, n):
    dimensions = subdivision(points, n)
    drawTriangle(points, window, color)

    #finds all the vertices of the triangles, ordered left to right and bottom to top
    midpoints = []
    for i in range(n + 1):
        start = addheight(addwidth(points[0], i * dimensions[0]/2), i * dimensions[1])
        midlevel = []
        for j in range(n-i+1):
            midlevel.append(addwidth(start, j * dimensions[0]))
        midpoints.append(midlevel)

    #draws all the white triangles
    midpoints.reverse()
    #whitetriangles = []
    for i in range(1,n):
        for j in range(i):
            temptri = []
            temptri.append(midpoints[i][j])
            temptri.append(midpoints[i][j+1])
            temptri.append(midpoints[i+1][j+1])
            #whitetriangles.append(temptri) to list the white triangles if desired
            drawTriangle(temptri, window, 'white')


    #finds the locations of all the black triangles, arranged left to right and bottom to top
    midpoints.reverse()
    blacktriangles = []
    for i in range(n+1):
        temptri = []
        for j in range(n-i):
            temptri.append([midpoints[i][j], midpoints[i+1][j], midpoints[i][j+1]])
        blacktriangles.append(temptri)

    if level > 0:
        for i in range(n):
            for j in range(n-i):
                if i !=1 :
                    sierpinski(blacktriangles[i][j], level - 1, window, color, n)

def main():
    depth = 4
    #set up the window using GraphWin
    window = GraphWin('Sierpinski Generalized Triangle', 1000, 866)
    #set the coordinates of the window
    window.setCoords(-201, -101, 201, 251)
    #list the starting points for the first square
    points = [Point(-200,-100), Point(0,250), Point(200,-100)]

    #call the function with the points
    sierpinski(points, depth, window, 'black', 3)
    #close the window when clicked
    window.getMouse()
    window.postscript(file = "sierp3.eps")
    window.close()


    img = NewImage.open("sierp3.eps")
    img.save("sierp3.png", "png")


main()
