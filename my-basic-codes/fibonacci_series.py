def fibonacci(n):
    # Initial two Fibonacci numbers
    a, b = 0, 1
    fib_series = []  # To store the Fibonacci series
    
    # Generating Fibonacci numbers up to n
    while a <= n:
        fib_series.append(a)
        a, b = b, a + b  # Update a and b to the next two numbers in the series
    
    return fib_series

# Taking input from the user
user_input = int(input("Enter a number: "))
fibo_series = fibonacci(user_input)
print("Fibonacci series up to", user_input, "is:", fibo_series)