import sys


def main():
    check_argv()
    try:
        with open(sys.argv[1]) as file:
            count = 0
            for line in file:
                if not line.isspace() and not line.lstrip().startswith("#"):
                    count += 1
        print (count)

    except FileNotFoundError:
        sys.exit("Error 1")


##
def check_argv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a Python File")


main()
