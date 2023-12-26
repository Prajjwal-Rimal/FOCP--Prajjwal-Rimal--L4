"""Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program.
"""


def main():
    x = input('Enter a string: ')
    print('The number of uppercase and lowercase characters are:', check(x))


u = 0
l = 0


def check(x):
    global u, l

    for char in x:
        if char.isupper():
            u = u + 1
        elif char.islower():
            l = l + 1
    return u, l


main()
