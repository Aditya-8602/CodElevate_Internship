'''
5. Given p dollars, the future value of this money when compounded yearly at a rate of r
percent interest for y years is p(1+0.01r)y. Write a Python statement that calculates and
prints the value of 1000 dollars compounded at 7 percent interest for 10 years. 

'''

p = 1000  
r = 7     
y = 10    

value = p * (1 + 0.01 * r) ** y

print(value)
