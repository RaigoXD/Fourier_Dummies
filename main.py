# Libraries to use
import sympy
from sympy import cos, sin
from sympy import pi
import matplotlib.pyplot as plt


def obtaining_a0(expressions_sympy, limits, periodo_T):
    # getting a0
    total_a0 = 0
    t = sympy.symbols('t')
    for index, sympy_expression in enumerate(expressions_sympy):
        total_a0 += sympy.integrate(sympy_expression, (t, limits[index][1], limits[index][0]))
    total_a0 = total_a0 * 2 / sympy.simplify(periodo_T)

    return total_a0

def obtaining_aN(expressions_sympy, limits, periodo_T, w0):
    # getting aN
    expression_aN = 0
    n = sympy.symbols('n')
    t = sympy.symbols('t')

    # Creating expressions with cos(n*w*t)
    expressions_an = [
        expression_sympy * cos(n*w0*t)
        for expression_sympy in expressions_sympy
    ]
    # Calculating the integral for all expressions and obtaining the final expression
    for index, expression_an in enumerate(expressions_an):
        expression_aN += sympy.integrate(expression_an, (t, limits[index][1], limits[index][0]))

    expression_aN = expression_aN * 2 / sympy.simplify(periodo_T)
    expression_aN = sympy.simplify(expression_aN)
    return expression_aN

def obtaining_bN(expressions_sympy, limits, periodo_T, w0):
    # getting bN
    expression_bN = 0
    n = sympy.symbols('n')
    t = sympy.symbols('t')

    # Creating expressions with cos(n*w*t)
    expressions_bn = [
        expression_sympy * sin(n*w0*t)
        for expression_sympy in expressions_sympy
    ]
    # Calculating the integral for all expressions and obtaining the final expression
    for index, expression_bn in enumerate(expressions_bn):
        expression_bN += sympy.integrate(expression_bn, (t, limits[index][1], limits[index][0]))

    expression_bN = expression_bN * 2 / sympy.simplify(periodo_T)
    expression_bN = sympy.simplify(expression_bN)
    return expression_bN

def calculating_f_x(expression_aN,expression_bN, total_a0, w0):
    n = sympy.symbols('n')
    t = sympy.symbols('t')
    # multiplying an and bn by cos(nwt) and sin(nwt) respectively
    expression_aN = expression_aN * cos(n*w0*t)
    expression_bN = expression_bN * sin(n*w0*t)
    # creating the function 
    f = (
        (total_a0 / 2) + sympy.summation(    
        expression_aN + expression_bN, 
        (n, 1, 10)
        )
    )
    # calculating the tabulation
    t_values = [i/30 for i in range(-100,100,1)]
    y_values = [f.evalf(subs={t:t_value}) for t_value in t_values]

    plt.plot(t_values, y_values)
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.title('Gráfica')
    plt.grid(True)
    plt.show()



if __name__ == '__main__': 
    periodo_T = input("Ingresa el periodo\n->")
    # Calc w
    w0 = 2*pi / sympy.simplify(periodo_T)
    # Getting the functions from keyboard 
    input_user = input("Ingresa la lista de las funciones, separadas por ,\n->")
    expressions = input_user.split(",")
    # expressions_sympy
    expressions_sympy = [sympy.simplify(expression) for expression in expressions]

    # obtaining limits 
    limits = []
    for expression in expressions:
        print(expression)
        limits.append(
            [sympy.simplify(input("limiteSuperior->")),sympy.simplify(input("limiteInferior->"))]
        )
    # calculating a0
    total_a0 = obtaining_a0(expressions_sympy,limits,periodo_T)
    expression_aN = obtaining_aN(expressions_sympy, limits, periodo_T, w0)
    expression_bN = obtaining_bN(expressions_sympy, limits, periodo_T, w0)

    print(f"\nEl resultado de a0 es: {total_a0} <--\n\n")
    sympy.pretty_print(expression_aN, use_unicode=True)
    print("\n\n")
    sympy.pretty_print(expression_bN, use_unicode=True)
    calculating_f_x(expression_aN,expression_bN, total_a0, w0)
