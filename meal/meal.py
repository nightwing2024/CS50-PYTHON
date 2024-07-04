# Convert
def convert(time):
    hours, minutes = time.split(":")
    time_float = float(hours) + float(minutes) / 60
    return time_float

# Main
def main():
    time = input("What time is it? ")
    time_float = convert(time)

    if 7 <= time_float <= 8:
        print("breakfast time")
    elif 12 <= time_float <= 13:
        print("lunch time")
    elif 18 <= time_float <= 19:
        print("dinner time")
    else:
        print("No meal time detected")

# Call
if __name__ == "__main__":
    main()
