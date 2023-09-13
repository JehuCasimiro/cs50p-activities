def main():
    amount_due = 50
    total_inserted = 0

    while total_inserted < amount_due:
        print("Amount Due:", amount_due - total_inserted)
        fee = int(input("Insert Coin: "))
        coin = calculate_coin(fee)

        if coin == 25 or coin == 10 or coin == 5:
            total_inserted += coin

    change_owed = total_inserted - amount_due
    print("Change Owed:", change_owed)

def calculate_coin(c):
    if c == 25:
        return 25
    elif c == 10:
        return 10
    elif c == 5:
        return 5
    else:
        return 0

main()
