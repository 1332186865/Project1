import turtle

colors = ['red', 'green', 'blue', 'purple']
turtle.speed(12)
turtle.width(3)
for o in range(4):
    c = colors[o]
    turtle.pencolor(c)
    turtle.right(360 / 4)
    turtle.circle(80)
    turtle.speed(6)
