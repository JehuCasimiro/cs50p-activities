def main():
    plate = input("Plate: ")
    if is_valid(plate) == True:
        print("Valid")
    elif is_valid(plate) == False:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() and len(s) >= 2 and len(s) <= 6:
        for c in s:
            if c.isdigit():
                index = s.index(c)
                if s[index:].isdigit() and int(c) != 0:
                    return True
                else:
                    return False
        return True
    return False


if __name__ == "__main__":
    main()