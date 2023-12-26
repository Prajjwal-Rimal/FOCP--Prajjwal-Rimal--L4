"""Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name differently. So if the user entered arthur, ARTHUR, or even
arTHur the name should be displayed as Arthur"""


def main():
    x = input('Enter a string: ')
    print('The number of uppercase and lowercase characters are:', string(x))


def string(x):
    x = x.lower()
    x = x.title()
    return x


main()
