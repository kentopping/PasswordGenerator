import random
import string
import os

def UI():
    while True:
        print("Welcome to my strong password generator!")
        print("1. Include Symbols(Y/N)?")
        symbol = loop()
        print("2. Include Numbers(Y/N)?")
        numbers = loop()
        print("3. Include Lowercase(Y/N)?")
        lowercase = loop()
        print("4. Include Uppercase(Y/N)?")
        uppercase = loop()
        if not symbol and not numbers and not lowercase and not uppercase:
            UI()
        password = get_password(15, symbol, numbers, lowercase, uppercase)
        print("\nSecure Password: ", password, "\n")

def loop():
    while True:
        n = input()
        if n == "Y" or n == "N" or n == "y" or n == "n":
            result = get_result(n)
            return result


def get_result(input):
    if input == "Y" or input == "y":
        return True
    else:
        return False

def test_pass(password, symbols, numbers, lowercase, uppercase):
    sym = False
    num = False
    low = False
    upp = False
    if symbols:
        for i in password:
            if i.isalnum():
                sym = True
    else:
        sym = True
    if numbers:
        for i in password:
            if i.isnumeric():
                num = True
    else:
        num = True
    if lowercase:
        for i in password:
            if i.islower():
                low = True
    else:
        low = True
    if uppercase:
        for i in password:
            if i.isupper():
                upp = True
    else:
        upp = True
    if sym and num and low and upp:
        return True
    else:
        return False

# returns a secure password based on the conditions given
def get_password(length, symbols, numbers, lowercase, uppercase):
    array = [symbols, numbers, lowercase, uppercase]
    newlist = []
    list_of_strings = [string.punctuation, string.digits, string.ascii_lowercase, string.ascii_uppercase]
    included = [i for i, x in enumerate(array) if x]
    for i in included:
        newlist.append(list_of_strings[i])
    while len(newlist) != 4:
        newlist.append("")
    while True:
        password = ''.join([random.choice(newlist[0] + newlist[1] + newlist[2] + newlist[3]) for n in range(length)])
        if test_pass(password, symbols, numbers, lowercase, uppercase):
            break
    return password


if __name__ == '__main__':
    UI()

