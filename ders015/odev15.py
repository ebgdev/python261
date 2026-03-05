import math

new_array = [i for i in range(1,101)]

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2,(number//2)+1):
        if number % i == 0:
            return False
    return True


primes = list(filter(lambda x: is_prime(x),new_array))
print(primes)