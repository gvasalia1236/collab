import re
import getpass
# Using ReGex for email and password validation
symbols = re.compile(r'[!@#$%^&*()_+={}\[\]:;"\'<>,.?/\\|`]')
pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
# Password validation
def passw():
    while True:
        password = getpass.getpass('Enter your password: ', stream=None)
        if len(password) < 8:
            print(f"\"{password}\" is too weak password")

        elif not re.search(r'\d', password):
            print(f"at least one digit in \"{password}\"")

        elif not symbols.search(password):
            print(f"at least one punctuation in \"{password}\"")

        else:
            print(f"\"{password}\" is valid password")
            break
# Email validation
def mail():
    while True:
        email = input("Enter your email: ")
        if re.fullmatch(pattern, email):
            print("Valid email")
            break

        elif not re.fullmatch(pattern, email):
            print("this kind of email doesnt exist!")

        else:
            print("succes")
            break
# Calling functions
passw()
mail()
