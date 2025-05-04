'''
1. Python program to calculate simple interest.

'''

P = int(input("Principal Amount: "))
R = int(input("Rate of interest: "))
T = int(input("Year: "))

SI = (P * R * T) / 100

print("Simple Intrest: ", SI)