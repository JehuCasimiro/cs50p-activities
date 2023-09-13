def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    result = float(d[1:])  # Remove the leading '$' and convert to float
    return result


def percent_to_float(p):
    result = float(p[:-1]) / 100  # Remove the trailing '%' and convert to float
    return result

main()