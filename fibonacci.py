'''def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 101):
    print(n, ":", fibonacci(n))
'''
# Need memoiszation: stores values from recent calls so similar calls do not have to repeat the work
n = int(input())
fibonacci_cache = {}

def fibonacci(n):
    #check that the input is an integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    # If we have cached the value, then return is
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # compute the nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # cache the value and return it
    fibonacci_cache[n] = value
    return value

'''for n in range(1, 51):
    print(n, ':', fibonacci(n))
'''

print(fibonacci(n))
