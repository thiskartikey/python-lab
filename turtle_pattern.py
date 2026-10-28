import turtle

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

num_sides = int(input("Enter number of sides: "))
side_len = int(input("Enter side length: "))

turn_angle = 360 / num_sides

for step in range(num_sides):
    pen.forward(side_len)
    pen.right(turn_angle)

def draw_koch(segment_len, level):
    if level == 0:
        pen.forward(segment_len)
    else:
        segment_len = segment_len / 3
        draw_koch(segment_len, level - 1)
        pen.left(60)
        draw_koch(segment_len, level - 1)
        pen.right(120)
        draw_koch(segment_len, level - 1)
        pen.left(60)
        draw_koch(segment_len, level - 1)

pen.penup()
pen.goto(-150, -100)
pen.pendown()

fractal_level = int(input("Enter Koch fractal depth: "))

for edge in range(3):
    draw_koch(300, fractal_level)
    pen.right(120)

turtle.done()
