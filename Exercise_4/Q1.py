'''
1. Write a password guessing program to keep track of how many times
the user has entered the password wrong. If it is more than 3 times,
print "You have been denied access." and terminate the program. If
the password is correct, print "You have successfully logged in." and
terminate the program.

'''
password = "mypassword"

attempts = 0
max_attempts = 3

while attempts < max_attempts:

    user_input = input("Enter your password: ")

    if user_input == password:
        print("You have successfully logged in.")
        break
    else:
        attempts += 1
        print("Incorrect password. Try again.")

    if attempts == max_attempts:
        print("You have been denied access.")
