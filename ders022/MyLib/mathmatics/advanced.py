def pow_2(a):
    return a**2


def pow_3(a):
    return a**3


def factorial(n):
    result = 1
    if n < 0:
        return("Invalid input. Please enter a positive integer.")
    elif n == 0:
        return 1
    else:
        for i in range(2,n+1): # n=4, 2,3,4
            result = result*i
        return result