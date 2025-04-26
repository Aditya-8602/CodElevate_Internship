'''
8. The distance between two points (x0, y0) and (x1, y1) is (x0-x1)2+(y0-y1)2
. Write a Python statement that calculates and prints the distance between the 
points (2,2) and (5,6). 

'''

import math

x0, y0 = 2, 2
x1, y1 = 5, 6

distance = math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
print(distance)
