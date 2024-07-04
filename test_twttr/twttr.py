print()


def main():
    """Hola"""
    string = input("Input: ")
    print("Output:", shorten(string), end="")


def shorten(word):
    """Hola"""
    result = ""
    for char in word:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            result += char
    return result


if __name__ == "__main__":
    main()
