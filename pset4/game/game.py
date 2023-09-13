import random

def main():
    while True:
        level = input("Level: ")

        if level.isdigit() and int(level) > 0:

            level = int(level)
            n = random.randint(1, level)

            while True:
                try:
                    guess = int(input("Guess: "))

                    if guess > n:
                        print("Too Large!")
                    elif guess < n:
                        print("Too Small!")
                    else:
                        print("Just Right!")
                        break
                except ValueError:
                    pass
            break
        else:
            pass

if __name__ == "__main__":
    main()