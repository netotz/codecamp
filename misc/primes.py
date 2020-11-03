# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.
# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

def is_prime(number, primes):
    for x in primes:
        if number % x == 0:
            return False
    return True

def get_primes(n):
    primes = []
    for number in range(2, n):
        if is_prime(number, primes):
            primes.append(number)
    return primes

def test_input():
    n = 35
    actual = get_primes(n)
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    assert actual == primes
