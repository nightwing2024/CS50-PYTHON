import sys
from datetime import date
import inflect

p = inflect.engine()

def main():
    try:
        fecha_nacimiento_str = input("Date of Birth: ")
    except ValueError:
        sys.exit("Invalid Date")

    fecha_nacimiento = convert(fecha_nacimiento_str)

    if fecha_nacimiento == "Invalid Date":
        sys.exit("Invalid Date")

    print(minutes_lived(fecha_nacimiento))


def convert(x):
    try:
        y, m, d = map(int, x.split('-'))
    except ValueError:
        return "Invalid Date"
    return date(y, m, d)


def minutes_lived(fecha_nacimiento):
    fecha_actual = date.today()

    diferencia = fecha_actual - fecha_nacimiento

    minutes = int(diferencia.total_seconds() / 60)

    msg = p.number_to_words(minutes, andword="")

    return f"{msg.capitalize()} minutes"


if __name__ == "__main__":
    main()
