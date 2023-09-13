import sys
import csv
from tabulate import tabulate


def main():
    check_args()

    items = []

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                # print(row)
                items.append(row)

            print(tabulate(items, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


def check_args():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few coomand-line arguments")
    else:
        pass

    if sys.argv[1].endswith(".csv") == False:
        sys.exit("Not a CSV file")
    else:
        pass


if __name__ == "__main__":
    main()