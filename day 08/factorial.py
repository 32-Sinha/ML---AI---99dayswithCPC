def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get input from the user
num = int(input("Enter a number: "))

# Calculate the factorial
result = factorial(num)

# Display the result
print(f"The factorial of {num} is {result}")
