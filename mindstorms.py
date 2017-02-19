import turtle

def main() :
    #initialize a screen
    window = turtle.Screen()
    window.bgcolor("red")

    drawSquare()
    drawCircle()
    drawTriangle()
    
    window.exitonclick()

def rotateSquare(someTurtle, angle) :

    #add some degree to the turle
    someTurtle.right(angle)


def drawSquare() :
    
    #draw square on the screen
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    for i in range(36) :
        for j in range(4) :
            #move forward on 100 pixel
            brad.forward(100)

            #rotates in-place for 90 degree clockwise
            brad.right(90)
            
        rotateSquare(brad, 10)

        
def drawCircle() :
    #Initialize instance of turtle named angie
    angie = turtle.Turtle()
    
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def drawTriangle() :
    #Initialize instance of turtle named dan
    dan = turtle.Turtle()

    dan.shape("classic")
    dan.color("green")

    dan.right(45)
    dan.forward(100)

    dan.right(135)
    dan.forward(130)

    dan.right(130)
    dan.forward(100)

main()
