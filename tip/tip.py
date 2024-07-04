def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    if dollars is not None and percent is not None:
        tip = dollars * percent
        print(f"Leave ${tip:.2f}")
    else:
        print("Invalid input. Please enter valid amounts.")

def dollars_to_float(d):
    return float(d.replace('$', ''))

def percent_to_float(p):
    return float(p.replace('%', '')) / 100

main()
