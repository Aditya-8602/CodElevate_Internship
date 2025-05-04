'''
2. Write a program that asks for two numbers. If the sum of the numbers
is greater than 100, print "That is a big number" and terminate the
program.

'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2

if total > 100:
    print("That is a big number")
