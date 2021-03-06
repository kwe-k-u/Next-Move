#graphics
from turtle import *
from tkinter import messagebox
from game import *

initial_dot=None
dot_radius=10

def squareToPoint(sq):
    if sq=="LeftTop":
        return(200, 400)
    elif sq=="RightTop":
        return(400,400)
    elif sq=="LeftBottom":
        return (200,200)
    elif sq=="RightBottom":
        return (400,200)

def hit(x,y):
    dot=None
    if 90<x<110 and 490<y<520:
        dot="Northwest"
    elif 290<x< 310 and 490<y<510:
        dot="North"
    elif 490<x< 510 and 490<y<510:
        dot="Northeast"
    elif 90<x<110 and 290<y<310:
        dot="West"
    elif 290<x<310 and 290<y<310:
        dot="Center"
    elif 490<x<510 and 290<y<310:
        dot="East"
    elif 90<x<110 and 90<y<110:
        dot="Southwest"
    elif 290<x<310 and 90<y<110:
        dot="South"
    elif 490<x<510 and 90<y<110:
        dot="Southeast"
    return dot

def dotToPoint(dot):
    if dot=="Northwest":
        return 100,500
    elif dot=="North":
        return 300,500
    elif dot=="Northeast":
        return 500,500
    elif dot=="West":
        return 100,300
    elif dot=="Center":
        return 300,300
    elif dot=="East" :
        return 500,300
    elif dot=="Southwest":
        return 100,100
    elif dot=="South":
        return 300,100
    elif dot=="Southeast":
        return 500,100

def drawDot(name, col="black"):
    global dot_radius
    pensize(1)
    penup()
    x,y=dotToPoint(name)
    setposition(x,y-dot_radius)
    pendown()
    color(col)
    begin_fill()
    circle(dot_radius)
    end_fill()
    update()

def drawLine(x1,y1,x2,y2):
    penup()
    setposition(x1,y1)
    pendown()
    setposition(x2,y2)
    update()

def drawX(x,y):
    color("blue")
    pensize(10)
    drawLine(x-40,y-40,x+40,y+40)
    drawLine(x-40,y-40,x+40,y+40)

def drawY(x,y):
    color("blue")
    pensize(10)
    drawLine(x-40,y-40,x+40,y+40)
    drawLine(x-40,y+40,x+40,y-40)
    drawLine(x,y,x,y-40)

def drawSquare(sq, owner):
    x,y= squareToPoint(sq)
    if owner=="X":
        drawX(x,y)
    elif owner=="Y":
        drawY(x,y)

def checkSquares():
    drawSquare("LeftTop", squareOwner("LeftTop"))
    drawSquare("RightTop", squareOwner("RightTop"))
    drawSquare("LeftBottom",squareOwner("LeftBottom"))
    drawSquare("RightBottom",squareOwner("RightBottom"))
    win=winner()
    if win=="X":
        messagebox.showinfo("Game Over", "X wins")
    elif win=="Y":
        messagebox.showinfo("Game Over", "Y wins")
    elif win=="Draw":
        messagebox.showinfo("Game Over, Tie Game")

def mouseClick(x,y):
    global initial_dot
    print("initial dot=", initial_dot)
    print("clicked at x=", x," y =",y)
    dot=hit(x,y)
    if dot:
        print(dot)
        if not initial_dot:
            initial_dot=dot
            drawDot(initial_dot, "red")
        elif dot!= initial_dot:
            if addLine(lineName(initial_dot,dot)):
                color("black")
                pensize(5)
                x1,y1=dotToPoint(initial_dot)
                x2,y2=dotToPoint(dot)
                drawLine(x1,y1,x2,y2)
                title("3x3 Connect the Dots Current Player: " + currentPlayer())
                checkSquares()
            drawDot(initial_dot)
            initial_dot=None
            drawDot(dot)
        else:
            if initial_dot:
                drawDot(initial_dot)
                initial_dot=None

def resetGame():#verified
    clearscreen()
    initialize()

def lineName(dot1,dot2):#verified
    if(dot1=="Northwest" and dot2=="North") or \
        (dot1=="North" and dot2=="Northwest"):
        return "NorthwestNorth"
    elif( dot1=="North" and dot2=="Northeast") or \
          (dot1=="Northeast" and dot2=="North"):
        return "NorthNortheast"
    elif (dot1=="Northwest" and dot2=="West") or\
         (dot1=="West" and dot2=="Northwest"):
        return "NorthwestWest"
    elif(dot1=="North" and dot2=="Center") or\
        (dot1=="Center" and dot2=="Center"):
        return "NorthCenter"
    elif (dot1=="Northeast" and dot2=="East") or \
         (dot1=="East" and dot2=="Northeast"):
        return "NortheastEast"
    elif (dot1=="West" and dot2=="Center") or\
         (dot1=="Center" and dot2=="West"):
        return "WestCenter"
    elif (dot1=="Center" and dot2=="East") or \
         (dot1=="East" and dot2=="Center"):
        return "CenterEast"
    elif (dot1=="West" and dot2=="Southwest") or\
         (dot1=="Southwest" and dot2=="West"):
        return "WestSouthwest"
    elif (dot1=="Center" and dot2=="South") or\
         (dot1=="South" and dot2=="Center"):
        return "CenterSouth"
    elif (dot1=="East" and dot2=="Southeast") or\
         (dot1=="Southeast" and dot2=="East"):
        return "EastSoutheast"
    elif (dot1=="Southwest" and dot2=="South") or\
         (dot1=="South" and dot2=="Southwest"):
        return "SouthwestSouth"
    elif (dot1=="South" and dot2=="Southeast") or\
         (dot1=="Southeast" and dot2=="South"):
        return "SouthSoutheast"
    elif (dot1=="Northwest" and dot2=="Center") or\
         (dot1=="Center" and dot2=="Northwest"):
        return "NorthwestCenter"
    elif (dot1=="Northeast" and dot2=="Center") or\
         (dot1=="Center" and dot2=="Northeast"):
        return "NortheastCenter"
    elif (dot1=="Southeast" and dot2=="Center") or\
         (dot1=="Center" and dot2=="Southeast"):
        return "SoutheastCenter"
    elif (dot1=="Southwest" and dot2=="Center") or\
         (dot1=="Center" and dot2=="Southwest"):
        return "SouthwestCenter"
    elif (dot1=="West" and dot2=="North") or\
         (dot1=="North" and dot2=="West"):
        return "NorthWest"
    elif (dot1=="North" and dot2=="East") or\
         (dot1=="East" and dot2=="North"):
        return "NorthEast"
    elif (dot1=="South" and dot2=="East") or\
         (dot1=="East" and dot2=="South"):
        return "SouthEast"
    elif (dot1=="South" and dot2=="West") or\
         (dot1=="West" and dot2=="South"):
        return "SouthWest"
    else:
        print("Nor a valid dot link")
        messagebox.showerror("Invalid Link","You may not connect those two dots")
        return None

def initialize():
    initializeBoard()
    screensize(600,600)
    setworldcoordinates(0,0,599,599)
    tracer(0)
    hideturtle()
    onscreenclick(mouseClick)
    onkeyrelease(resetGame,"q")
    listen()
    title("3x3 Connect the Dots    Current Player: "+ currentPlayer())
    initial_dot=None
    for dot in ("Northwest", "North", "Northeast", "West", "Center", "East", "Southwest", "South", "Southeast"):
        drawDot(dot)
        update()

if __name__== "__main__":
    initialize()
    mainloop()
    
