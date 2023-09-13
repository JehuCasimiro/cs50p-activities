def main():
    get_grocery()

def get_grocery():

    groceries = {}

    while True:
        try:
            item = input("").upper()

            if item in groceries:
                groceries[item] += 1
            elif item == "":
                pass
            else:
                groceries[item] = 1

        except EOFError:
            print("")
            break

    for i in sorted(groceries.keys()):
            print(groceries[i], i)

main()