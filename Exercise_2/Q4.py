'''
4. Take input from a user that is age and check eligibility 
for voting or not.

'''

age = int(input("Enter Age: "))

if (age >= 18 and age <= 100):
    print("Eligible for voting.")
elif(age <= 18):
    print("Not eligible for voting.")
else:
    print("Enter valid age.")