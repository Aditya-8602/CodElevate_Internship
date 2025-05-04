'''
5. Python program to convert temperature from Fahrenheit to Celsius.

'''
frh = float(input("Enter temperature in Fahrenheit: "))

cels = (frh - 32) * 5 / 9

print(f"{frh}°F is equal to {cels:.2f}°C")