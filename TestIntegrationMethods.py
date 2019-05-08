import numpy as np
from IntegrationTechniques import Integration

def f(x):
    return x

def g(x):
    return x**2 + 2*x

def h(x):
    return np.cos(x) + 1/2

def main():
    integration = Integration()
    print(50)
    print(integration.composite_simpson(0, 10, f, 10))

    print(10**3/3 + 100)
    print(integration.composite_simpson(0, 10, g, 10))

    print(integration.composite_simpson(0, np.pi/2, h, 10))
    #print(integration.simpson_rule(0, np.pi/2, h, 9))

    print("User Input")
    x = 2
    funct = eval(input("Please input a function(x): "))

    print(funct)
main()