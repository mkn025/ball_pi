


# formula that solves a quadratic equation
def quadratic(a, b, c):
    """
    Solves a quadratic equation.
    """
    if a == 0:
        return "a must not be zero"
    else:
        x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
        x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
        return x1, x2

print(quadratic(-4.9,12,2))