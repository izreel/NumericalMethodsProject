import numpy as np
from numpy import cos, sin, tan, arccos, arcsin, arctan, exp, pi, log
from scipy.misc import derivative


class Integration:
    def __init__(self):
        self.function_string = ''

    def set_function_string(self, input_function):
        self.function_string = input_function

    def funct(self, x):
        return eval(self.function_string)

    def midpoint_rule(self, a, b, f, n):
        self.set_function_string(f)
        h = (b - a) / (n + 2)
        error = (h ** 3) / 3 * derivative(self.funct, (b + a) / 2, dx=0.1, n=2, order=3)

        return 2 * h * self.funct((a + b) / 2), error

    def trapezoidal_rule(self, a, b, f):
        self.set_function_string(f)
        h = b - a
        error = -(h ** 3) / 12 * derivative(self.funct, (b + a) / 2, dx=0.1, n=2, order=3)

        return (h / 2) * (self.funct(a) + self.funct(b)), error

    def simpson_rule(self, a, b, f):
        self.set_function_string(f)
        h = (b - a) / 2
        error = -(h ** 5) / 90 * derivative(self.funct, (b + a) / 2, dx=0.1, n=4, order=5)

        return (h / 3) * (self.funct(a) + 4 * self.funct(a + h) + self.funct(b)), error

    def composite_midpoint_rule(self, a, b, f, n):
        '''Performs the Midpoint Rule or Rectangular Integration on interval [a,b]
            :param f: function f that will be integrated
            :param n: number of subintervals in [a,b]
            :return: integration of function f on interval [a,b]
        '''
        self.set_function_string(f)
        h = (b - a) / (n + 2)
        final_sum = 0

        for i in range(0, int(n / 2) + 1):
            x = a + (i+1) * h
            final_sum += self.funct(x)

        error = ((b - a) / 6) * (h ** 2) * derivative(self.funct, (b + a) / 2, dx=0.1, n=2, order=3)
        return final_sum * h*2, error

    def composite_trapezoidal_rule(self, a, b, f, n):
        '''Performs the Midpoint Rule or Rectangular Integration on interval [a,b]
            :param f: function f that will be integrated
            :param n: number of subintervals in [a,b]
            :return: integration of function f on interval [a,b]
        '''
        self.set_function_string(f)
        h = (b - a) / n
        temp_xa = self.funct(a)
        temp_xb = self.funct(b)

        final_sum = (temp_xa + temp_xb)

        for i in range(1, n):
            x = a + i * h
            final_sum += self.funct(x)

        error = -((b - a) / 12) * (h ** 2) * derivative(self.funct, (b + a) / 2, dx=0.1, n=2, order=3)
        return final_sum * h / 2, error

    def composite_simpson_rule(self, a, b, f, n):
        '''Performs Composite Simpson technique on interval [a,b]
            :param f: function f that will be integrated
            :param n: number of subintervals in [a,b]
            :return: integration of function f on interval [a,b]
        '''
        self.set_function_string(f)

        h = (b - a) / n
        temp_xa = self.funct(a)
        temp_xb = self.funct(b)
        x0 = temp_xa + temp_xb
        x1 = 0
        x2 = 0

        for i in range(n):
            x = a + i * h
            if i % 2 == 0:
                x2 += self.funct(x)
            else:
                x1 += self.funct(x)

        error = -(b - a) / 180 * (h ** 4) * derivative(self.funct, float((b + a) / 2), dx=0.1, n=4, order=5)
        return h * (x0 + 2 * x2 + 4 * x1) / 3, error
