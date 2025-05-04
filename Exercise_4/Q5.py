'''
5. Program to print a Fibonacci Series.

'''
n = int(input("Enter number: "))

# first two terms
a, b = 0, 1

# check if number is valid
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci Series:", a)
else:
    print("Fibonacci Series:", end=" ")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b  # Update values 
