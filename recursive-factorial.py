def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return (n * recursive_factorial(n-1))


number = 125
print(f"The factorial of {number} is {recursive_factorial(number)}.")