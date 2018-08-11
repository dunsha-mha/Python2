import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("yellow")
    
    moe = turtle.Turtle()
    moe.shape("turtle")
    turtle.shapesize()
    (50,50,50)
    moe.color("red","white")
    moe.speed(10)
   
    line = 1
    square = 4

    while line <= square: 
        moe.forward(400)
        moe.left(90)

        line = line + 1
    
draw_square()

def draw_circle():
   
    sarah = turtle.Turtle()
    sarah.shape("turtle")
    turtle.shapesize()
    (60,60,60)
    sarah.color("blue")
    sarah.speed(10)
   
    sarah.forward(200)
    sarah.circle(199)

draw_circle()

def draw_triangle():

    right_tri = turtle.Turtle()
    right_tri.shape("arrow")
    right_tri.shapesize()
    (60,60,60)
    right_tri.color("green","white")
    right_tri.speed(10)
    right_tri.left(45)
    right_tri.forward(85)
    right_tri.left(23)
    right_tri.forward(363)
    right_tri.left(225)
    right_tri.forward(370)
    right_tri.right(113)
    right_tri.forward(282)


draw_triangle()

window.exitonclick()
