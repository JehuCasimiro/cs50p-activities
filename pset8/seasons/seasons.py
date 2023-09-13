from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    print(calculate(input("Date of Birth: ")))


def calculate(birthdate):
    if matches := re.search(r"^([0-9][0-9][0-9][0-9])-([0-9][0-9])-([0-9][0-9])$", birthdate):
        year, month, day = matches.groups()

        if 2023 > int(year) > 0 and 0 < int(month) < 13 and 0 < int(day) < 32:
            difference = date.today() - date.fromisoformat(f"{year}-{month}-{day}")
            total_minutes = difference.total_seconds() / 60
            words = p.number_to_words(int(total_minutes), andword="")

            return f"{words.capitalize()} minutes"
        else:
            return "Invalid date"
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()