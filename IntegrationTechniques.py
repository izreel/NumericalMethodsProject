import numpy as np
from numpy import cos, sin, tan, arccos, arcsin, arctan, exp, pi, sqrt
from scipy.misc import derivative


def funct(function_string, x):
    return eval(function_string)

class Integration:
    def midpoint_rule(self, a, b, f, n):
        h = (b-a)/(n+2)
        error = (h**3) / 3 * derivative(funct, (b + a) / 2, dx=0.1, n=2)

    def trapezoidal_rule(self, a, b, f):
        h = b - a
        error = -(h ** 3) / 12 * derivative(funct, (b + a) / 2, dx=0.1, n=2)

        return (h/2)*(funct(f, a) + funct(f, b)), error

    def simpson_rule(self, a, b, f):
        h = (b-a)/2
        error = -(h**5) / 90 * derivative(funct, (b + a) / 2, dx=0.1, n=4)

        return (h/3)*(funct(f, a) + 4 * funct(f, a + h) + funct(f, b)), error

    def composite_midpoint_rule(self, a, b, f, n):
        '''Performs the Midpoint Rule or Rectangular Integration on interval [a,b]
            :param f: function f that will be integrated
            :param n: number of subintervals in [a,b]
            :return: integration of function f on interval [a,b]
        '''
        h = (b - a) / (n + 2)
        final_sum = 0

        for i in range(0, int(n/2)+1):
            x = a + i * h
            final_sum += funct(f, x)

        error = ((b-a)/6) * (h**2) * derivative(funct, (b+a)/2, dx= 0.1, n=2)
        return final_sum * h, error

    def composite_trapezoidal_rule(self, a, b, f, n):
        '''Performs the Midpoint Rule or Rectangular Integration on interval [a,b]
            :param f: function f that will be integrated
            :param n: number of subintervals in [a,b]
            :return: integration of function f on interval [a,b]
        '''
        h = (b - a) / n
        temp_xa = funct(f, a)
        temp_xb = funct(f, b)

        final_sum = (temp_xa + temp_xb)

        for i in range(1, n):
            x = a + i * h
            final_sum += funct(f, x)

        error = -((b-a)/12) * (h**2) * derivative(funct, (b + a) / 2, dx=0.1, n=2)
        return final_sum * h/2, error


    def composite_simpson(self, a, b, f, n):
        '''Performs Composite Simpson technique on interval [a,b]
            :param f: function f that will be integrated
            :param n: number of subintervals in [a,b]
            :return: integration of function f on interval [a,b]
        '''
        h = (b - a) / n
        temp_xa = funct(f, a)
        temp_xb = funct(f, b)
        x0 = temp_xa + temp_xb
        x1 = 0
        x2 = 0

        for i in range(n):
            x = a + i * h
            if i % 2 == 0:
                x2 += funct(f, x)
            else:
                x1 += funct(f, x)

        error =  -(b-a)/180 * (h**4) * derivative(funct, (b+a)/2, dx= 0.1, n=4)
        return h * (x0 + 2 * x2 + 4 * x1) / 3, error

    

