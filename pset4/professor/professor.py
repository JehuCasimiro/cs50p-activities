import random

def main():
    score = 0
    level = get_level()

    for _ in range(10):
        tries = 0
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        while tries < 3:
            try:
                user_input = int(input(f"{x} + {y} = "))
                if user_input == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
                    pass

            except ValueError:
                print("EEE")
                tries += 1
                pass

        if tries == 3:
            print(f"{x} + {y} = {answer}")
            pass

    print("Score:", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                pass
        except ValueError:
            pass

def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()