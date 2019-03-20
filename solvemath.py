""" Demonstrate use of Python for symbolic math using the SymPy package.

SymPy: https://www.sympy.org/en/index.html

Examples of using the SymPy package to solve equations and calculate
derivatives.
"""

import sympy

sympy.init_printing(use_unicode=True)

x, y = sympy.symbols('x y')

#solve an eqaution for x
xval = sympy.solveset(sympy.Eq(x+5, 0), x)

# most of the lines here are to print results nicely
# very few lines are needed for the actual computation
print('\nsolve for x:')
sympy.pprint(sympy.Eq(x+5, 0))
print('\nx is equal to')
sympy.pprint(xval)

#solve another equation for x
xval = sympy.solveset(sympy.Eq(x**2, 2), x)
print('\nsolve for x:')
sympy.pprint(sympy.Eq(x**2, 2))
print('x is equal to')
sympy.pprint(xval)

#solve an equation for y
equation = sympy.Eq(x, 2*y+5)
yexpression = sympy.solveset(equation, y)
print('\nsolve for y:')
sympy.pprint(equation)
print('\ny is equal to:')
sympy.pprint(yexpression)

#take the derivative of a trig function
equation = sympy.cos(x)
deriv = sympy.diff(equation, x)
print('\nThe derivative of')
sympy.pprint(equation)
print('is')
sympy.pprint(deriv, use_unicode=True)

#take the derivative of another expression
equation = sympy.exp(x**2)
deriv = sympy.diff(equation, x)
print('\nThe derivative of')
sympy.pprint(equation)
print('is')
sympy.pprint(deriv, use_unicode=True)
