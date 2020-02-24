# Case-study 1
# Developers: Moiseenko V.( 69 %)
#             Vlasov V.( 31 %)
# This programm allows to draw different fractal pictures

import turtle

# For Victoria: draw the Koch curve
def koch_curve(l, n):
    if n == 0:
        turtle.forward(l)
    else:
        koch_curve(l/3, n-1)
        turtle.left(60)
        koch_curve(l/3, n-1)
        turtle.right(120)
        koch_curve(l/3, n-1)
        turtle.left(60)
        koch_curve(l/3, n-1)

# For Vlas: draw the Koch snowflake
def koch_snowflake():
    pass

# For Victoria: draw the ice fractal (example 1)
def ice_fractal1(l, n):
    if n == 0:
        turtle.forward(l)
    else:
        ice_fractal1(l/2, n-1)
        turtle.left(120)
        ice_fractal1(l/4, n-1)
        turtle.right(180)
        ice_fractal1(l/4, n-1)
        turtle.left(120)
        ice_fractal1(l/4, n-1)
        turtle.right(180)
        ice_fractal1(l/4, n-1)
        turtle.left(120)
        ice_fractal1(l/2, n-1)


# For Vlas: draw the ice fractal (example 2)
def ice_fractal2(l, n):
    if n == 0:
        turtle.forward(l)
    else:
        ice_fractal2(l / 2, n - 1)
        turtle.left(90)
        ice_fractal2(l / 4, n - 1)
        turtle.left(180)
        ice_fractal2(l / 4, n - 1)
        turtle.left(90)
        ice_fractal2(l / 2, n - 1)

# For Victoria: draw the binary tree fractal
def binary_tree(l,n):
    if count == 0:
        turtle.left(90)
    if n == 0:
        return

    turtle.down()
    turtle.forward(l)
    turtle.right(20)

    count += 1

    binary_tree(l * 0.9, n - 1, count)
    turtle.left(40)
    binary_tree(l * 0.9, n - 1, count)
    turtle.right(20)
    turtle.backward(l)


# For Vlas: draw the branch fractal
def branch():
    pass

# For Victoria: draw the Minkovsky curve
def minkovsky_curve(l,n):
    if n == 0:
        turtle.forward(l)
    else:
        minkovsky_curve(l/6, n-1)
        turtle.left(90)
        minkovsky_curve(l/6, n-1)
        turtle.right(90)
        minkovsky_curve(l/6, n-1)
        turtle.right(90)
        minkovsky_curve(l/3, n-1)
        turtle.left(90)
        minkovsky_curve(l/6, n-1)
        turtle.left(90)
        minkovsky_curve(l/6, n-1)
        turtle.right(90)
        minkovsky_curve(l/6,n-1)


# For Victoria: draw the Levi curve
def levi_curve(l, n):
    if n == 0:
        turtle.forward(l)
        return
    else:
        turtle.left(45)
        levi_curve(l, n - 1)
        turtle.right(45)
        turtle.right(45)
        levi_curve(l, n - 1)
        turtle.left(45)

def main():
    turtle.up()
    turtle.goto(-200, 0)
    turtle.down()
    name = str(input('Enter the name of fractal: '))
    l = int(input('Enter the length: '))
    n = int(input('Enter the  depth: '))
    if name == 'Koch Curve':
        koch_curve(l, n)
    elif name == 'Koch Snowflake':
        koch_snowflake()
    elif name == 'Ice Fractal 1':
        ice_fractal1(l, n)
    elif name == 'Ice Fractal 2':
        ice_fractal2()
    elif name == 'Binary Tree':
        binary_tree(l, n)
    elif name == 'Branch':
        branch()
    elif name == 'Minkovsky Curve':
        minkovsky_curve(l, n)
    elif name == 'Levi Curve':
        levi_curve(l, n)

main()

turtle.done()