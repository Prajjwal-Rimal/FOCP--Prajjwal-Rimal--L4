"""Write a program that simulates the way in which a user might choose a password.
The program should prompt for a new password, and then prompt again. If the two
passwords entered are the same the program should say "Password Set" or
similar, otherwise it should report an error"""


def main():
    x = str(input("enter a password: "))
    y = str(input("re enter the password: "))
    return password(x, y)


def password(x, y):
    if x == y:
        print("PASSWORD SET")
    else:
        print("ERROR SETTING THE PASSWORD")


main()
