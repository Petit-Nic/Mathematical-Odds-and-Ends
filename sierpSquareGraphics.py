from graphics import *

def drawSquare(points, window, color):
    square = Rectangle(points[0], points[1])
    square.setWidth(0)
    square.setFill(color)
    square.draw(window)

def sierpinskiCarpet(points, level, window, color):

    if level == 0:
        square = Rectangle(points[0], points[1])
        square.setWidth(0)
        square.setFill(color)
        square.draw(window)
    else:

        x_0 = (points[0].getX())
        x_02 = (points[1].getX())
        x_1 = (((points[0].getX())/3)*2 +  (points[1].getX())/3)
        x_2 = (((points[0].getX())/3)   + ((points[1].getX())/3)*2)

        y_0 = (points[0].getY())
        y_02 = (points[1].getY())
        y_1 = (((points[0].getY())/3)*2 +  (points[1].getY())/3)
        y_2 = (((points[0].getY())/3)   + ((points[1].getY())/3)*2)


        top1 = [points[0], Point(x_1, y_1)]
        top2 = [Point(x_1, y_0), Point(x_2, y_1)]
        top3 = [Point(x_2, y_0), Point(x_02, y_1)]

        med1 = [Point(x_0, y_1), Point(x_1, y_2)]
        med2 = [Point(x_1, y_1), Point(x_2, y_2)]
        med3 = [Point(x_2, y_1), Point(x_02, y_2)]

        bottom1 = [Point(x_0, y_2), Point(x_1, y_02)]
        bottom2 = [Point(x_1, y_2), Point(x_2, y_02)]
        bottom3 = [Point(x_2, y_2), points[1]]

# sierpinskiCarpet(SQUARE, level - 1, window, color) to draw repeating pattern
#  drawSquare(SQUARE, window, color) to draw solid square
# Comment out sierpinskiCarpet to draw white repeating square

        sierpinskiCarpet(top1, level - 1, window, color)
        drawSquare(top2, window, color)
        sierpinskiCarpet(top3, level - 1, window, color)
        sierpinskiCarpet(med1, level - 1, window, color)
        sierpinskiCarpet(med2, level - 1, window, color)
        sierpinskiCarpet(med3, level - 1, window, color)
#        sierpinskiCarpet(bottom1, level - 1, window, color)
        sierpinskiCarpet(bottom2, level - 1, window, color)
        sierpinskiCarpet(bottom3, level - 1, window, color)


def main():
    #get the depth from the system arguments
    depth = 6
    #set up the window using GraphWin
    window = GraphWin('Sierpinski Carpet', 1000, 1000)
    #set the coordinates of the window
    window.setCoords(-0.1, -0.1, 1.1, 1.1)
    #list the starting points for the first square
    points = [Point(0, 1), Point(1, 0)]

    #call the function with the points
    sierpinskiCarpet(points, depth, window, 'black')
    #close the window when clicked
    window.getMouse()
    window.close()

main()
