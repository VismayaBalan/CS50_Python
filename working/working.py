import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^([1]?[0-9]|[2][0-4])(:[0-5][0-9])? (AM|PM) to ([1]?[0-9]|[2][0-4])(:[0-5][0-9])? (AM|PM)$",s,re.IGNORECASE)
    if matches:
        start_hr = int(matches.group(1))
        end_hr = int(matches.group(4))
        start_min = matches.group(2)
        end_min = matches.group(5)
        start_period = matches.group(3)
        end_period = matches.group(6)

        if start_period.lower() == 'pm' and start_hr > 12:
            raise ValueError
        if end_period.lower() == 'pm' and end_hr > 12:
            raise ValueError

        if start_period.lower() == 'am' and start_hr == 12:
            start_hr -= 12

        if start_period.lower() == 'pm' and start_hr < 12:
            start_hr += 12
        if end_period.lower() == 'pm' and end_hr < 12:
            end_hr += 12
        if start_min == None and end_min == None:
            return f"{start_hr:02}:00 to {end_hr:02}:00"
        else:
            return f"{start_hr:02}{start_min} to {end_hr:02}{end_min}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()