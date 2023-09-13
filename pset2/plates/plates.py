def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() and len(s) >= 2 and len(s) <= 6:
            if not any(c in "!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~" for c in s):
                for c in s:
                    if c.isdigit():
                        index = s.index(c)
                        if s[index:].isdigit() and int(c) != 0:
                            return True
                        else:
                            return False
                return True

main()