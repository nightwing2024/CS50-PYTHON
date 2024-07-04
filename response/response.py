from validator_collection import validators, checkers

user_input = input("Email: ").strip()

try:
    email_address = validators.email(user_input)

    is_email_address = checkers.is_email(email_address)

    if is_email_address is True:
        print("Valid")
    else:
        pass
except ValueError:
    print ("Invalid")
