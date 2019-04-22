class Integration:
    def composite_simpson(self, a, b, f, n):
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
