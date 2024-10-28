## Implement a Recursive Fibonacci Generator
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Testing the recursive function
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")

## Implement an Iterative Fibonacci Generator
def fibonacci_iterative(n):
    if n <= 1:
        return n
    first, second = 0, 1
    for _ in range(2, n + 1):
        first, second = second, first + second
    return second

# Testing the iterative function
for i in range(10):
    print(f"F({i}) = {fibonacci_iterative(i)}")

import time

## Compare Performance
def measure_time(func, n): 
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

# Testing both functions and comparing execution times
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")

## Implement a Generator Function for Fibonacci Sequence
def fibonacci_generator(limit):
    first, second = 0, 1
    count = 0
    while count < limit:
        yield first
        first, second = second, first + second
        count += 1

# Testing the generator function
for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i}) = {fib}")

## Implement Memoization for Recursive Fibonacci
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

# Testing the memoized function
for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")

# Compare performance with the original recursive function
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")

             ## Exercises
# Question 1: Modify the iterative function to return a list of Fibonacci numbers up to n, instead of just the nth number.
def list_of_fibonacci(x):
    if x <= 0:
        return [0]
    elif x == 1:
        return [0, 1]
    fibonacci_listing = [0, 1]
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
        fibonacci_listing.append(b)
    return fibonacci_listing

# Testing the function
print(list_of_fibonacci(10))

# Question 2: Implement a function that finds the index of the first Fibonacci number that exceeds a given value.
def index_of_first_fibonacci(target):
    a, b = 0, 1
    position = 1
    while b <= target:
        a, b = b , a + b
        position += 1
    return position

# Testing the function
print(index_of_first_fibonacci(100))

# Question 3: Create a function that determines if a given number is a Fibonacci number.
def checking_fibonacci(number):
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    return b == number

# Testing the function
print(checking_fibonacci(13))  # True
print(checking_fibonacci(14))  # False

# Question 4: Implement a function that calculates the ratio between consecutive Fibonacci numbers and observe how it approaches the golden ratio.
def calculate_fibonacci_ratios(max):
    a, b = 0, 1
    fibonacci_ratios = []
    for _ in range(max - 1):
        if a != 0:
            fibonacci_ratios.append(b/ a)
        a, b = b, a + b
    return fibonacci_ratios

# Testing the function
print(calculate_fibonacci_ratios(10))

