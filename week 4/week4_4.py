"""When processing data it is often useful to remove the last character from some
input (it is often a newline). Write and test a function that takes a string parameter
and returns it with the last character removed. (If the string contains one or fewer
characters, return it unchanged."""


def main():
    x = input('Enter a string: ')
    print('The final version of string is:', string(x))


def string(x):
    if len(x) <= 1:
        return x
    else:
        x = x[:len(x) - 1]
        return x


main()
