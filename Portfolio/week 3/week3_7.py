"""Modify your "Times Table" program so that the user enters the number of the table
they require. This number should be between 0 and 12 inclusive"""


def main():
    y = int(input("enter the range required from 1 to 12:   "))
    print("The table of 7 is:", table(y))


def table(y):
    for x in range(0, y + 1):
        print(f"{x} x 7 = {x * 7}")


main()
