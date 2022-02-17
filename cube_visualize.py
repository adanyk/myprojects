import turtle
from cube import *



t = turtle.Turtle()
t.width(3)
t.speed(0)
t.hideturtle()
turtle.tracer(0,0)


def cube_to_colors(cube):
    colors = []
    for sticker in cube:
        if sticker == 'w':
            colors.append('white')
        elif sticker == 'o':
            colors.append('orange')
        elif sticker == 'g':
            colors.append('green')
        elif sticker == 'r':
            colors.append('red')
        elif sticker == 'b':
            colors.append('blue')
        elif sticker == 'y':
            colors.append('yellow')
    return colors


def draw_sticker(color):
    t.pendown()
    t.color('black', color)
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()
    t.penup()

def draw_u_sticker(color):
    t.pendown()
    t.color('black', color)
    t.begin_fill()
    for i in range(2):
        t.forward(50)
        t.right(135)
        t.forward(25)
        t.right(45)
    t.end_fill()
    t.penup()

def draw_r_sticker(color):
    t.pendown()
    t.color('black', color)
    t.begin_fill()
    for i in range(2):
        t.forward(25)
        t.right(135)
        t.forward(50)
        t.right(45)
    t.end_fill()
    t.penup()


def draw_u_face(face):
    for i, c in enumerate(face):
        draw_u_sticker(c)
        if (i + 1) % 3 == 0:
            t.backward(100)
            t.left(45)
            t.backward(25)
            t.right(45)
        else:
            t.forward(50)

def draw_r_face(face):
    t.left(45)
    for i, c in enumerate(face):
        draw_r_sticker(c)
        if (i + 1) % 3 == 0:
            t.backward(50)
            t.left(45)
            t.backward(50)
            t.right(45)
        else:
            t.forward(25)

def draw_f_face(face):
    for i, c in enumerate(face):
        draw_sticker(c)
        if (i + 1) % 3 == 0:
            t.backward(100)
            t.right(90)
            t.forward(50)
            t.left(90)
        else:
            t.forward(50)




def draw_2d_cube(cube):
    colors = cube_to_colors(cube)
    t.penup()
    t.backward(150)
    t.left(90)
    t.forward(250)
    t.right(90)

    for i, c in enumerate(colors):
        draw_sticker(c)
        if i == 8:
            t.backward(250)
            t.right(90)
            t.forward(50)
            t.left(90)
        elif i == 44:
            t.backward(400)
            t.right(90)
            t.forward(50)
            t.left(90)
        elif (i + 1) % 9 == 0:
            t.forward(50)
            t.left(90)
            t.forward(100)
            t.right(90)
        elif (i + 1) % 3 == 0:
            t.backward(100)
            t.right(90)
            t.forward(50)
            t.left(90)
        else:
            t.forward(50)

def draw_3d_cube(cube):
    colors = cube_to_colors(cube)
    t.penup()
    t.backward(50)
    t.left(90)
    t.forward(50)
    t.right(90)

    draw_u_face(colors[:9])
    t.backward(125)
    draw_r_face(colors[11:8:-1] + colors[14:11:-1] + colors[17:14:-1])
    t.right(45)
    t.forward(125)
    t.left(90)
    t.forward(150)
    t.right(90)
    draw_f_face(colors[18:27])
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.right(90)
    draw_r_face(colors[27:36])
    t.forward(150)
    t.left(45)
    t.forward(150)
    t.right(90)
    draw_f_face(colors[38:35:-1] + colors[41:38:-1] + colors[44:41:-1])
    t.left(45)
    t.backward(75)
    t.right(45)
    t.backward(150)
    t.left(90)
    t.backward(125)
    t.right(90)
    draw_u_face(colors[51:] + colors[48:51] + colors[45:48])







if __name__ == "__main__":

    mix = generate_scramble(n=25)
    mixed_cube = do_simple_scramble(solved, mix)
    print(mix)


    # draw_3d_cube(mixed_cube)
    draw_2d_cube(mixed_cube)


    turtle.update()
    turtle.done()
