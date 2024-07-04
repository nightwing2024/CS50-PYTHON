import csv
from tabulate import tabulate
import sys

menu = []

def main():
    check_argv()
    try:
        with open (sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)

        print (tabulate(menu[1:],headers=menu[0],tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


def check_argv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

main ()
