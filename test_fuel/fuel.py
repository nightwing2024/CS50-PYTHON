def main():
    user_input = input("Fraction: ")
    fraction_converted = convert(user_input)
    output = gauge(fraction_converted)

    print(output)


def convert(fraction):
    while True:
        try:
            num, den = map(int,fraction.split("/"))

            f = num / den
            if f <= 1:
                p = int(f * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
