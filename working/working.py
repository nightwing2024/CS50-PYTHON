import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.match(r"^([0-9][0-2]?):?([0-5][0-9])? (AM|PM)? to ([0-9][0-2]?):?([0-5][0-9])? (AM|PM)?$", s)
    if not match:
        raise ValueError("Invalid input format")

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    start_hour = int(start_hour)
    end_hour = int(end_hour)

    if start_hour > 12 or end_hour > 12:
        raise ValueError

    if start_period == "PM" and start_hour != 12:
        start_hour += 12
    elif start_period == "AM" and start_hour == 12:
        start_hour = 0

    if end_period == "PM" and end_hour != 12:
        end_hour += 12
    elif end_period == "AM" and end_hour == 12:
        end_hour = 0

    start_time = f"{start_hour:02}:{start_minute or '00'}"
    end_time = f"{end_hour:02}:{end_minute or '00'}"

    return f"{start_time} to {end_time}"

if __name__ == "__main__":
    main()
