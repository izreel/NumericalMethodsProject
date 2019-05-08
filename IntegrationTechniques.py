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
            final_sum += f(x)

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
            temp = a + i * h
            final_sum += f(temp)

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
            final_sum = f(x)

        return final_sum * h    

    def composite_midpoint(self, a, b, f, n):
        '''
        Performs Composite Simpson technique on interval [a,b]
        :param f: function f that will be integrated
        :param n: number of subintervals in [a,b]
        :return: integration of function f on interval [a,b]
        '''
        h = (b - a) / n
        x0 = f(a) + f(b)
        x1 = 0
        x2 = 0

        for i in range(n):
            x = a + i * h
            if i % 2 == 0:
                x2 += f(x)
            else:
                x1 += f(x)

        return h * (x0 + 2 * x2 + 4 * x1) / 3

    def composite_trapezoidal(self, a, b, f, n):
        '''
        Performs Composite Simpson technique on interval [a,b]
        :param f: function f that will be integrated
        :param n: number of subintervals in [a,b]
        :return: integration of function f on interval [a,b]
        '''
        h = (b - a) / n
        x0 = f(a) + f(b)
        x1 = 0
        x2 = 0

        for i in range(n):
            x = a + i * h
            if i % 2 == 0:
                x2 += f(x)
            else:
                x1 += f(x)

        return h * (x0 + 2 * x2 + 4 * x1) / 3

    def composite_simpson(self, a, b, f, n):
        '''
        Performs Composite Simpson technique on interval [a,b]
        :param f: function f that will be integrated
        :param n: number of subintervals in [a,b]
        :return: integration of function f on interval [a,b]
        '''
        h = (b - a) / n
        x0 = f(a) + f(b)
        x1 = 0
        x2 = 0

        for i in range(n):
            x = a + i * h
            if i % 2 == 0:
                x2 += f(x)
            else:
                x1 += f(x)

        return h * (x0 + 2 * x2 + 4 * x1) / 3    

    
