import sys

def main():
    valid_lines = 0
    check_args()

    try:
        with open(sys.argv[1], 'r') as file:
            lines = file.readlines()
            for line in lines:
                if check_code(line) == True:
                    pass
                elif check_code(line) == False:
                    valid_lines += 1
                else:
                    pass
                
            print(valid_lines)

    except FileNotFoundError:
        sys.exit("File does not exist")


def check_args():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few coomand-line arguments")
    else:
        pass

    if sys.argv[1].endswith(".py") == False:
        sys.exit("Not a Python file")
    else:
        pass

def check_code(line):
    if line.isspace():
        return True
    elif line.lstrip().startswith("#"):
        return True
    else:
        return False


if __name__ == "__main__":
    main()