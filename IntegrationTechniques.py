import numpy as np

#used when user inputs one of the following functions
#will call the numpy implementation of the function
def cos(x):
    return np.cos(x)

def sin(x):
    return np.sin(x)

def exp(x):
    return np.e

def pi(x):
    return np.pi

class Integration:
    def midpoint_rule(self, a, b, f, n):
        '''Performs the Midpoint Rule or Rectangular Integration on interval [a,b]
            :param f: function f that will be integrated
            :param n: number of subintervals in [a,b]
            :return: integration of function f on interval [a,b]
        '''
        h = (b - a) / n
        final_sum = 0

        for i in range(1, n + 1):
            x = 0.5 * (2 * a + h * (2 * i -1))
            final_sum += eval(f)

        return final_sum * h
    
    def trapezoidal_rule(self, a, b, f, n):
        '''Performs the Midpoint Rule or Rectangular Integration on interval [a,b]
            :param f: function f that will be integrated
            :param n: number of subintervals in [a,b]
            :return: integration of function f on interval [a,b]
        '''
        h = (b - a) / n
        final_sum = f(a) + f(b)

        for i in range(1, n + 1):
            x = a + i * h
            final_sum += eval(f)

        return final_sum * h / 2

    def simpson_rule(self, a, b, f, n):
        '''Performs the Midpoint Rule or Rectangular Integration on interval [a,b]
            :param f: function f that will be integrated
            :param n: number of subintervals in [a,b]
            :return: integration of function f on interval [a,b]
        '''
        h = (b - a) / n
        final_sum = f(a) + f(b)
        if n % 2:
            raise ValueError("N must be even for Simpson's Rule")

        for i in range(1, n + 1):
            x = 0.5 * (2 * a + h * (2 * i -1))
            final_sum = eval(f)

        return final_sum * h

    def composite_simpson(self, a, b, f, n):
        '''Performs Composite Simpson technique on interval [a,b]
            :param f: function f that will be integrated
            :param n: number of subintervals in [a,b]
            :return: integration of function f on interval [a,b]
        '''
        h = (b - a) / n
        x = a
        temp_xa = eval(f);
        x = b
        temp_xb = eval(f);
        x0 = temp_xa + temp_xb
        x1 = 0
        x2 = 0
        for i in range(n):
            x = a + i * h
            if i % 2 == 0:
                x2 += eval(f)
            else:
                x1 += eval(f)
        return h * (x0 + 2 * x2 + 4 * x1) / 3    

    

