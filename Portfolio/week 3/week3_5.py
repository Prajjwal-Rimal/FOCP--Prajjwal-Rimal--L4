"""Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time"""


def main():
    while True:
        x = str(input("enter a password: "))
        y = str(input("re enter the password: "))
        result = password(x, y)
        print(result)
        if result == "PASSWORD SET":
            break


BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']


def password(x, y):
    if x in BAD_PASSWORDS:
        return "THIS PASSWORD IS A BAD PASSWORD, CHOOSE ANOTHER PASSWORD"
    elif len(x) < 8 or len(x) > 12:
        return "INAPPROPRIATE LENGTH"
    elif x != y:
        return "PASSWORD DOESNT MATCH" # all failure condition grouped and positive elsed
    else:
        return "PASSWORD SET"


main()
