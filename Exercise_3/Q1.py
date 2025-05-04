'''
1. Print all numbers between 1 to 1000 which are divisible by 9 and
must not be divisible by 3.

'''

for num in range(1, 1001):
    #check if the number is divisible by 9 but not by 3
    if num % 9 == 0 and num % 3 != 0:
        print(num, end=" ")

# every number that is divisible by 9 is also divisible by 3
# there will be no output for this program
# because such a number does not exist