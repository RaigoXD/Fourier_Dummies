# Libraries to use
import sympy
from sympy import cos, sin
from sympy import pi
import math
import numpy as np

#schemas
from backend.schemes.schemes import Function 

class FunctionOperations:

    def tabulate_function(function: Function):
        t = sympy.Symbol('t')
        function_sympy = sympy.simplify(function.function)
        upper_limit = float(sympy.simplify(function.upper_limit))
        lower_limit = float(sympy.simplify(function.lower_limit))
        print(function_sympy, upper_limit, lower_limit)
        
        values_t = [i for i in np.arange(lower_limit,upper_limit+0.1, 0.1)]
        y_values = [
            float(function_sympy.evalf(subs={t : t_value}))
            for t_value in values_t
        ]
        print(y_values)

        data_response = {
            "t_values": values_t,
            "y_values": y_values
        } 
        return data_response 