from numpy import cos, sin, tan, arccos, arcsin, arctan, exp, pi, sqrt
from IntegrationTechniques import Integration

def f():
    return 'x'

def g():
    return 'x**2 + 2*x'

def h():
    return 'cos(x) + 1/2'

def main():
    integration = Integration()
    print(50)
    print(integration.composite_simpson_rule(0, 10, f(), 10))

    print(10**3/3 + 100)
    print(integration.composite_simpson_rule(0, 10, g(), 10))

    #print(integration.simpson_rule(0, np.pi/2, h, 9))
    print(eval("exp(4)"))
    # print("User Input")
    # x = 2
    # funct = eval(input("Please input a function(x): "))
    #
    # print(funct)

main()