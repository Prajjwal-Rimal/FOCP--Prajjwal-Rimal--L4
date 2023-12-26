'''write a program that prompts a user to enter a temperature in Celsius, and then
displays the corresponding temperature in Fahrenheit, like so:
Enter a temperature in Celsius: 32.5
32.5C is equivalent to 90.5F'''

c = float(input('Input the temperature in celsius: '))
f = c * (9 / 5) + 32
print(f'Hello the temperature is {f} degree Fahrenheit.!')
