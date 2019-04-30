class Integration:
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
