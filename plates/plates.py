def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check the length of the string
    if not (2 <= len(s) <= 6):
        return False

    # Check that the string starts with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Check that if there are numbers, they are at the end and the first number is not '0'
    has_number = False
    for i in range(2, len(s)):
        if s[i].isdigit():
            has_number = True
        elif has_number: # If there is a number followed by a letter, the string is invalid
            return False

    if has_number and s[2] == '0': # If the first number is '0', the string is invalid
        return False

    # Check that no periods, spaces, or punctuation marks are allowed
    for char in s:
        if not char.isalnum():
            return False

    return True

main()
