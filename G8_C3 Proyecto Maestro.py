import turtle

longitud = 10

while longitud <= 150:
    for i in range(10):
        turtle.pencolor('red')
        turtle.forward(longitud)
        turtle.right(89)
        longitud += 0.5
        break
    turtle.pencolor('green')
    turtle.forward(longitud)
    turtle.right(89)
    longitud += 0.5
