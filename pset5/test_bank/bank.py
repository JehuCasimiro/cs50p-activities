def main():
    greeting = input("Enter a greeting: ")
    value(greeting)


def value(g):
    greet = g.strip()

    if greet.startswith("hello") | greet.startswith("Hello"):
        print("$0")
        return 0
    elif greet.startswith("h") | greet.startswith("H"):
        print("$20")
        return 20
    else:
        print("$100")
        return 100


if __name__ == "__main__":
    main()