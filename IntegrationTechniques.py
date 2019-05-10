import numpy as np
from numpy import cos, sin, tan, arccos, arcsin, arctan, exp, pi, sqrt, log
from scipy.misc import derivative


class Integration:
    def __init__(self):
        self.function_string = ''

    def set_function_string(self, input_function):
        '''
        Sets user's input function as class member
        :param input_function:string containing user input
        '''
        self.function_string = input_function

    def funct(self, x):
        '''
        Runs function_string as python code which in this case is a mathematical function
        :param x: value to plug in to function (ie f(x))
        :return: return value of function_string(x)
        '''
        return eval(self.function_string)

    def midpoint_rule(self, a, b, f):
        '''
        Performs Midpoint rule over interval [a, b]
        :param a: lower bound of interval
        :param b: higher bound of interval
        :param f: function to be integrated
        :return: integration result of f over [a,b] and its error
        '''
        self.set_function_string(f)
        h = (b - a) / (2)

        # calculates the error for the method uses the midpoint of the interval to pass to f(n)(x)
        error = (h ** 3) / 3 * derivative(self.funct, (b + a) / 2, dx=0.1, n=2, order=3)

        return 2*h*self.funct(h), error

    def trapezoidal_rule(self, a, b, f):
        '''
        Performs Trapezoidal rule over interval [a, b]
        :param a: lower bound of interval
        :param b: higher bound of interval
        :param f: function to be integrated
        :return: integration result of f over [a,b] and its error
        '''
        self.set_function_string(f)
        h = b - a

        # calculates the error for the method uses the midpoint of the interval to pass to f(n)(x)
        error = -(h ** 3) / 12 * derivative(self.funct, (b + a) / 2, dx=0.1, n=2, order=3)

        return (h / 2) * (self.funct(a) + self.funct(b)), error

    def simpson_rule(self, a, b, f):
        '''
        Performs Simpson rule over interval [a, b]
        :param a: lower bound of interval
        :param b: higher bound of interval
        :param f: function to be integrated
        :return: integration result of f over [a,b] and its error
        '''
        self.set_function_string(f)
        h = (b - a) / 2

        # calculates the error for the method uses the midpoint of the interval to pass to f(n)(x)
        error = -(h ** 5) / 90 * derivative(self.funct, (b + a) / 2, dx=0.1, n=4, order=5)

        return (h / 3) * (self.funct(a) + 4 * self.funct(a + h) + self.funct(b)), error

    def composite_midpoint_rule(self, a, b, f, n):
        '''
        Performs the Composite Midpoint Rule Integration on interval [a,b]
        :param f: function f that will be integrated
        :param n: number of subintervals in [a,b]
        :return: integration of function f on interval [a,b] and its error
        '''
        self.set_function_string(f)
        h = (b - a) / (n + 2)
        final_sum = 0

        """
        Will go through from 0 to n+1 and sum up all f(x) for each subinterval where i % 2 = 0
        """
        for i in range(n + 2):
            x = a + (i + 1) * h
            if (i % 2 == 0):
                final_sum += self.funct(x);

        # calculates the error for the method uses the midpoint of the interval to pass to f(n)(x)
        error = ((b - a) / 6) * (h ** 2) * derivative(self.funct, (b + a) / 2, dx=0.1, n=2, order=3)

        return final_sum * 2*h, error

    def composite_trapezoidal_rule(self, a, b, f, n):
        '''
            Performs the Composite Trapezoidal Rule Integration on interval [a,b]
            :param f: function f that will be integrated
            :param n: number of subintervals in [a,b]
            :return: integration of function f on interval [a,b] and error
        '''
        self.set_function_string(f)
        h = (b - a) / n
        temp_xa = self.funct(a)
        temp_xb = self.funct(b)
        final_sum = 0

        """
            Takes the sum of all f(x) in each subinterval in [a, b]
        """
        for i in range(1, n):
            x = a + i * h
            final_sum += self.funct(x)

        # calculates the error for the method uses the midpoint of the interval to pass to f(n)(x)
        error = -((b - a) / 12) * (h ** 2) * derivative(self.funct, (b + a) / 2, dx=0.1, n=2, order=3)

        return (2*final_sum + temp_xa + temp_xb) * h / 2, error

    def composite_simpson_rule(self, a, b, f, n):
        '''Performs Composite Simpson technique on interval [a,b]
            :param f: function f that will be integrated
            :param n: number of subintervals in [a,b]
            :return: integration of function f on interval [a,b] and error
        '''
        self.set_function_string(f)

        h = (b - a) / n
        temp_xa = self.funct(a)
        temp_xb = self.funct(b)
        x0 = temp_xa + temp_xb
        x1 = 0
        x2 = 0

        '''
            Goes through each subinterval in [a,b] and determines whether is i is even or odd
            Depending whether i is even or odd, we will add f(x) to either x2 or x1
        '''
        for i in range(1,n):
            x = a + i * h
            if i % 2 == 0:
                x2 += self.funct(x)
            else:
                x1 += self.funct(x)

        # calculates the error for the method uses the midpoint of the interval to pass to f(n)(x)
        error = -(b - a) / 180 * (h ** 4) * derivative(self.funct, (b + a) / 2, dx=0.1, n=4, order=5)

        return h * (x0 + 2 * x2 + 4 * x1) / 3, error
