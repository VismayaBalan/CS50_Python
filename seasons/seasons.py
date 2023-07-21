from datetime import date, datetime
import sys
import operator
import inflect


def main():
    try:
        year, month, day = input("Date of Birth: ").split("-")
    except ValueError:
        sys.exit("Invalid date")
    print(f"{num_words(minutes_lived(year,month,day))} minutes".capitalize())


def minutes_lived(year,month,day):
    try:
        today = date.today()
        birth = date(int(year),int(month),int(day))
    except ValueError:
        sys.exit("Invalid date")
    diff = operator.__sub__(today,birth)
    minutes = diff.days * 24 * 60
    return minutes

def num_words(minutes):
    p = inflect.engine()
    words = p.number_to_words(int(minutes),andword="")
    return words

if __name__ == '__main__':
    main()




