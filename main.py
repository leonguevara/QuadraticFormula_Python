#   main.py
#   QuadraticFormula_Python
#
#   This program will ask the user for two whole numbers and two real numbers.  It will show
#   the addition, subtraction, multiplication, division and remainder of division of the two
#   whole numbers, as well as the division of both numbers treated as real numbers.
#
#   It will also show the addition, subtraction, multiplication and division of the two real
#   numbers.
#
#   Python interpreter: 3.6
#
#   Author: León Felipe Guevara Chávez
#   email:  leon.guevara@itesm.mx
#   date:   May 28, 2017
#

import sqrt from math         # We import the math library to use the sqrt() function

#   We ask for and read the values of a, b and c
a = float(input("Give me the value of a:"))
b = float(input("Give me the value of b:"))
c = float(input("Give me the value of c:"))

#   We compute and display the first possible value of x
x = (-b + sqrt(b**2 - 4*a*c))/(2*a)
print("x1 = " + str(x))

#   We compute and display the second possible value of x
x = (-b - sqrt(b**2 - 4*a*c))/(2*a)
print("x2 = " + str(x))
