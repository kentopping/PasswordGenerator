import random
import string

'''
This is the main user interface for my program.
'''


def UI():
    while True:
        print("Welcome to my strong password generator!")
        print("1. How long would you like your password(minimum 5 characters)?")
        length = input()

        while not length.isnumeric() or int(length) < 5:
            print("Password must be an number and at least 5 characters long")
            length = input()

        print("1. Include Symbols(Y/N)?")
        symbol = loop()
        print("2. Include Numbers(Y/N)?")
        numbers = loop()
        print("3. Include Lowercase(Y/N)?")
        lowercase = loop()
        print("4. Include Uppercase(Y/N)?")
        uppercase = loop()

        # This if statement calls UI if none of the parameters are true to create a password
        if not symbol and not numbers and not lowercase and not uppercase:
            UI()
        password = get_password(length, symbol, numbers, lowercase, uppercase)
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


'''
This function tests the given password to ensure that the password includes the correct components expected.
'''


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


'''
This function creates a strong random password based on the inputs of the user
'''


def get_password(length, symbols, numbers, lowercase, uppercase):
    list_of_booleans = [symbols, numbers, lowercase, uppercase]
    final_list = []
    list_of_strings = [string.punctuation, string.digits, string.ascii_lowercase, string.ascii_uppercase]
    included = [i for i, x in enumerate(list_of_booleans) if x]
    for i in included:
        final_list.append(list_of_strings[i])
    while len(final_list) != 4:
        final_list.append("")
    while True:
        password = ''.join(
            [random.choice(final_list[0] + final_list[1] + final_list[2] + final_list[3]) for n in range(length)])
        if test_pass(password, symbols, numbers, lowercase, uppercase):
            break
    return password


if __name__ == '__main__':
    UI()
