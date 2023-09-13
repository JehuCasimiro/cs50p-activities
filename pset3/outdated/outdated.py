def main():
    get_date()

def get_date():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            date = input("Date: ")

            if "/" in date:
                m, d, y = map(int, date.split("/"))

                if 1 <= m <= 12 and 1 <= d <= 31:
                    break

            elif "," in date:
                date = date.replace(",", "")
                m, d, y = date.split(" ")

                if m in months:
                    m = months.index(m) + 1
                    d = int(d)

                    if 1 <= d <= 31:
                        break

        except (ValueError, IndexError):
            pass

    print(f"{y:02}-{m:02}-{d:02}")

main()
