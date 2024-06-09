
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def sin(x,n):
    print(sum([((-1)**i) * (x**(2*i+1))/factorial(2*i+1) for i in range(n)]))

def cos(x,n):
    print(sum([((-1)**i) * (x**(2*i))/factorial(2*i) for i in range(n)]))

def sinh(x,n):
    print(sum([(x**(2*i+1))/factorial(2*i+1) for i in range(n)]))

def cosh(x,n):
    print(sum([(x**(2*i))/factorial(2*i) for i in range(n)]))