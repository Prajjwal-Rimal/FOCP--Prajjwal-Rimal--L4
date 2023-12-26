"""Modify your program again so that the chosen password cannot be one of a list of
common passwords, defined thus:
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']"""


def main():
    x = str(input("enter a password: "))
    y = str(input("re enter the password: "))
    return password(x, y)


BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']


def password(x, y):
    if x in BAD_PASSWORDS:
        print("THIS PASSWORD IS A BAD PASSWORD, CHOOSE ANOTHER PASSWORD")

    else:
        if 8 <= len(x) <= 12:
            if x == y:
                print("PASSWORD SET")
            else:
                print("ERROR SETTING THE PASSWORD")
        else:
            print("INAPPROPRIATE LENGTH")


main()
