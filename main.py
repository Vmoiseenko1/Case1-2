# Case-study 1
# Developers: Moiseenko V.( %)
#             Vlasov V.( %)
# This programm allows to draw different fractal pictures

import turtle

# For both: draw the binary tree
def binary_tree():
    pass

# For Victoria: draw the Koch curve
def koch_curve(l,n):
    if n == 0:
        turtle.forward(l)
    else:
        koch_curve(l/3,n-1)
        turtle.left(60)
        koch_curve(l/3,n-1)
        turtle.right(120)
        koch_curve(l/3,n-1)
        turtle.left(60)
        koch_curve(l/3,n-1)



# For Vlas: draw the Koch snowflake
def koch_snowflake():
    pass

# For Victoria: draw the ice fractal (example 1)
def ice_fractal1():
    pass

# For Vlas: draw the ice fractal (example 2)
def ice_fractal2():
    pass

# For Victoria: draw the snowflake for the first ice fractal
def snowflake_ice1():
    pass

# For Vlas: draw the snowflake for the second ice fractal
def snowflake_ice2():
    pass

# For Victoria: draw the Minkovsky curve
def minkovsky_curve():
    pass

# For Vlas: draw the Levi curve 
def levi_curve():
    pass

def main():
    turtle.up()
    turtle.goto(-200, 0)
    turtle.down()
    binary_tree()
    l = int(input('Enter the length:'))
    n = int(input('Enter the  depth:'))
    koch_curve(l,n)
    koch_snowflake()
    ice_fractal1()
    ice_fractal2()
    snowflake_ice1()
    snowflake_ice2()
    minkovsky_curve()
    levi_curve()


main()

turtle.done()