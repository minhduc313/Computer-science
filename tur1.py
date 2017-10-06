import turtle
import time

def initialise():
    canvas = turtle.Screen()
    canvas.title("Flag-It")
    soup = turtle.Turtle()
    soup.penup()
    soup.color("hotpink")
    return soup

#create functions here to draw lines and then functions to call these for the various numbers in your barcode.
pen = initialise()
pen.down()
def square():
    for n in range(0,4):
        pen.forward(90)
        pen.right(90)
def triangle():
    for n in range (0,1):
        pen.left(60)
        pen.forward(90)
        pen.right(120)
        pen.forward(90)
def laos():
    for n in range (0,2):
        pen.fillcolor("red")
        pen.begin_fill()
        pen.forward(240)
        pen.left(90)
        pen.forward(160)
        pen.left(90)
        pen.end_fill()
    pen.left(90)
    pen.forward(40)
    pen.right(90)
    for n in range (0,2):
        pen.fillcolor("blue")
        pen.begin_fill()
        pen.forward(240)
        pen.left(90)
        pen.forward(80)
        pen.left(90)
        pen.end_fill()
    pen.forward(120)
    pen.fillcolor("white")
    pen.begin_fill()
    pen.circle(40)
    pen.end_fill()

def vietnam():
    for n in range(0,2):
        pen.fillcolor("red")
        pen.begin_fill()
        pen.forward(240)
        pen.left(90)
        pen.forward(160)
        pen.left(90)
        pen.end_fill()
    pen.left(90)
    pen.forward(106.66)
    pen.right(90)
    pen.up()
    pen.forward(75)
    pen.begin_fill()
    for n in range(0,5):
        pen.fillcolor("yellow")
        pen.forward(96)
        pen.right(144)
    pen.end_fill()
def nagornokarabakh():
    pen.penup()
    for n in range (0,2):
        pen.fillcolor("red")
        pen.begin_fill()
        pen.forward(240)
        pen.left(90)
        pen.forward(106.66)
        pen.left(90)
        pen.end_fill()
    for n in range (0,2):
        pen.fillcolor("blue")
        pen.begin_fill()
        pen.forward(240)
        pen.left(90)
        pen.forward(71.106)
        pen.left(90)
        pen.end_fill()
    for n in range (0,2):
        pen.fillcolor("yellow")
        pen.begin_fill()
        pen.forward(240)
        pen.left(90)
        pen.forward(35.55)
        pen.left(90)
        pen.end_fill()
    pen.forward(240)
    pen.left(90)
    pen.forward(106.66)
    pen.left(90)
    for n in range(0,2):
        pen.fillcolor("white")
        pen.begin_fill()
        pen.forward



nagornokarabakh()



time.sleep(5)

