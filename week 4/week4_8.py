"""Modify the previous program so that it can process any number of values. The input
terminates when the user just pressed "Enter" at the prompt rather than entering a
value"""


def main():
    a = []
    for i in range(6):
        temperature = float(input("Enter temperature: "))
        a.append(temperature)
    print('The maximum, minimum, and mean temperatures are:', calculate(a))


def calculate(a):
    max_temperature = max(a)
    min_temperature = min(a)
    mean_temperature = sum(a) / len(a)
    return max_temperature, min_temperature, mean_temperature


main()
