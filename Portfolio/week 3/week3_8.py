"""Modify the "Times Table" again so that the user still enters the number of the table,
but if this number is negative the table is printed backwards. So entering "-7"
would produce the Seven Times Table starting at "12 times" down to "0 times"""


def main():
    y = int(input("enter the range required from 1 to 12:   "))
    print("The table of 7 is:", table(y))


def table(y):
    if y < 0:
        y = abs(y)
        for x in range(y, -1, -1): # sep size use otherwise program confuse
            print(f"{x} x 7 = {x * 7}")
    else:
        for x in range(0, y + 1):
            print(f"{x} x 7 = {x * 7}")


main()
