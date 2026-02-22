import math

def f(x):
    return 2*x - 5
#2x - 5
def g(x):
    return x**2 - 3*x + 1 
#x² - 3x + 1

def h(x):
    if x >= 0:
        print("valeur interdite")
    else:
        return math.sqrt(x)


#√x
x = float(input("Donne la valeur pour x: "))

print("f(x) =", f(x))
print("g(x) =", g(x))
print("h(x) =", h(x))
