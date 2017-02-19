import turtle

def main() :
    #Initilize window
    window = turtle.Screen()

    #Initialize an flower instance
    flower = turtle.Turtle()
    flower.shape("turtle")
    flower.color("yellow")
    flower.speed(0)

    stem = turtle.Turtle()
    stem.shape("arrow")
    stem.color("green")
               
    drawFractalFlower(flower, stem)

    window.exitonclick()

def drawFractalFlower(flowerObject, stemObject) :

    for petals in range (360):
        for petal in range(4) :
            flowerObject.forward(80)
            flowerObject.right(90)

        flowerObject.right(1)

    stemObject.right(90)
    stemObject.forward(200)
    

main()
