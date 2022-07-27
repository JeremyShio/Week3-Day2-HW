from math import pi

def radius():
    r = float(input ("Input the radius of the circle : "))
    print(pi * r**2)

radius()



from math import sqrt

def hypotenuse():
    print("Input lengths of shorter triangle sides:")
    a = float(input("a: "))
    b = float(input("b: "))
    c = sqrt(a**2 + b**2)
    print(c)

hypotenuse()