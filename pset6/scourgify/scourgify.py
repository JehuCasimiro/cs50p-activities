import sys
import csv
from tabulate import tabulate


def main():
    check_args()

    students = []

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].strip().split(",")
                house = row["house"]

                student = {"first": first.strip(), "last": last, "house": house}
                students.append(student)

        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first","last","house"])
            writer.writeheader()
            for student in students:
                writer.writerow(student)


    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


def check_args():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few coomand-line arguments")
    else:
        pass

    if sys.argv[2].endswith(".csv") == False:
        sys.exit("Not a CSV file")
    else:
        pass


if __name__ == "__main__":
    main()