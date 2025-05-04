'''
5. Design a simple calculator using if - elif - else statements.

'''

a = int(input("Enter first number: "))
op = int(input("Enter an operator (+, -, *, /, %): "))
b = int(input("Enter second number: "))

if op == "+":
    print("Addition: ",a+b)
elif op == "-":
    print("Subtraction: ",a-b)
elif op == "*":
    print("Multiplication: ",a*b)
elif op == "/":
    if b != 0:
        print("Division: ",a/b)
    else:
        print("Division by zero is not allowed!")
elif op == "%":
    if b != 0:
        print("Modulus: ",a%b)
    else:
        print("Modulus by zero is not allowed!")
else:
    print("Invalid operator! Please enter +, -, *, /, or %.")
