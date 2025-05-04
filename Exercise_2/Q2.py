'''
2. Python program to calculate compound interest.

'''
P = int(input("Principal amount: ")) 
R = int(input("Rate of interest: ")) 
T = int(input("Year: "))  


A = P * (1 + R / 100) ** T  # Final amount
CI = A - P  # Compound Interest

print("Compound Interest:", round(CI, 2))
