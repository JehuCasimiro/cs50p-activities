def main():
    fraction = convert(input("Fraction: "))
    output = gauge(fraction)
    print(output)


def convert(fraction):
    while True:
        try:
            x, y = map(int, fraction.split("/"))
            f = x / y

            if f <= 1:
                percent = int(f * 100)
                return percent
            else:
                pass

        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()


