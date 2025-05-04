'''
3. Python program to check whether the given number is a prime
number or not.

'''
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):  #check divisibility up to sqrt(num)
        if num % i == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a Prime Number")
else:
    print(num, "is NOT a prime number")
