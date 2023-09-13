def main():
    get_fraction()

def get_fraction():
    while True:
        try:
            x, y = map(int, input("Fraction: ").split("/"))
            result = x / y * 100

            if x > y:
                pass
            elif result <= 1:
                print("E")
                break
            elif result >= 99:
                print("F")
                break
            else:
                print(f"{result:.0f}%")
                break

        except (ValueError, ZeroDivisionError):
            pass

main()