import turtle

bob = turtle.Turtle()
josh = turtle.Turtle()
b = turtle.Turtle()


def square(turtle_object, length, side):
    turn = 360/side

    for i in range(side):
         turtle_object.fd(length)
         turtle_object.lt(turn)
    turtle.mainloop()


square(bob, 50, 9)


