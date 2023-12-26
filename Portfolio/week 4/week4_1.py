"""Functions are often used to validate input. Write a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise. Write a short program to test the function"""


def main():
    x = int(input('enter a number: '))
    print('The number lies in the range od 1-100:', check(x))


def check(x):
    if x not in range(0, 101):
        return False
    else:
        return True


main()
