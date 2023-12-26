""" Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long."""


def main():
    x = str(input("enter a password: "))
    y = str(input("re enter the password: "))
    return password(x, y)


def password(x, y):
    if 8 <= len(x) <= 12:
        if x == y:
            print("PASSWORD SET")
        else:
            print("ERROR SETTING THE PASSWORD")
    else:
        print("INAPPROPRIATE LENGTH")


main()
