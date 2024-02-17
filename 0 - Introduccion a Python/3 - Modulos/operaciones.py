def factorial_it(n):
    factorial = 1
    for i in range(n,1,-1):
        factorial = factorial * i
    return factorial