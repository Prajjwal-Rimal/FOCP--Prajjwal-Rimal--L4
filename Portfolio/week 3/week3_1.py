"""Modify your greeting program so that if the user does not enter a name (i.e. they
just press enter), the program responds "Hello, Stranger!". Otherwise, it should print
a greeting with their name as before."""


def main():
    x = str(input("enter your name: "))
    return greet(x)


def greet(x):
    if x != "":  # if x is not equal to empty
        print("Welcome", x)
    else:
        print("Hello Stranger")


main()
