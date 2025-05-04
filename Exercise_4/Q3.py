'''
3. Write a program to check whether the given string is palindrome or not?

'''
string = input("Enter a string: ")

# lowercase to make it case-insensitive
string = string.lower()

# to check reverse string
if string == string[::-1]:
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")
