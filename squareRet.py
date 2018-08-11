import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("yellow")
    
    moe = turtle.Turtle()
    moe.shape("turtle")
    turtle.shapesize()
    (50,50,50)
    moe.color("red","white")
    moe.speed(1)
   
    
    moe.forward(100)
    moe.left(90)
    moe.forward(100)
    moe.left(90)
    moe.forward(100)
    moe.left(90)
    moe.forward(100)
    moe.left(90)
    
    window.exitonclick()
    
draw_square()
