def main ():

    x = get_porcentaje()

    if x <= 1:
            print("E")
    elif x >= 99:
            print("F")
    else:
        print(x,"%",sep="")



def get_porcentaje():
    while True:
        try:
            # Ask user for input
            fraction = (input("Fraction: "))

            # Split the input and conver to int
            num,deno = map(int,fraction.split("/"))

            if num > deno:
                continue

            # Convert to %
            division = round(num / deno * 100)

            break

        except (ValueError, ZeroDivisionError):
            pass


    return division

main()
