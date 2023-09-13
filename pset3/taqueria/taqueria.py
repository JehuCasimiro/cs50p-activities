def main():
    get_order()

def get_order():

    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total_order = 0

    while True:
        try:
            item = input("Item: ").title()
            order = menu[item]
            total_order += order

            print(f"Total: ${total_order:.2f}")
        except KeyError:
            pass
        except EOFError:
            print("")
            break

main()
