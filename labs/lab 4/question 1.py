def factorial(n):
    result = 1  # Initialize the result to 1
    for i in range(n, 0, -1):  # Start from n and decrement down to 1
        result *= i  # Multiply result by i in each iteration
    return result

# Example usage:
number = 5
result = factorial(number)
print(f"{number}! = {result}")
