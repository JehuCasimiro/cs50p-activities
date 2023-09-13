def main():
    greeting = input("Enter a greeting: ")
    greet(greeting)

def greet(g):
    greet = g.strip()

    if greet.startswith("hello") | greet.startswith("Hello"):
        print("$0")
    elif greet.startswith("h") | greet.startswith("H"):
        print("$20")
    else:
        print("$100")

main()