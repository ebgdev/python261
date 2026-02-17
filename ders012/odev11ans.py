# Faktoriyel fonksiyonu yaziniz:

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

print(factorial(-5))  # Invalid input. Please enter a positive integer.
print(factorial(1))  # Output: 1
print(factorial(0))  # Output: 1
print(factorial(5))  # Output: 120 1*2*3*4*5


