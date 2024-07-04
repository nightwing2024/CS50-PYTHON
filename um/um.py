import re


def main():
    print(count(input("Text: ")))


def count(s):
    word = "um"
    ocurrencias = re.findall(r"\b" + re.escape(word) + r"\b", s, flags=re.IGNORECASE)
    return len(ocurrencias)


if __name__ == "__main__":
    main()
