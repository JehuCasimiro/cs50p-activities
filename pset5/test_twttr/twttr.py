def main():
    string = input("Input: ")
    new_string = shorten(string)
    print("Output:", new_string)


def shorten(word):
    new_string = ""
    for char in word:
        if (char == 'a' or char == 'e' or char == 'i' or
        char == 'o' or char == 'u' or char == 'A' or
        char == 'E' or char == 'I' or char == 'O' or
        char == 'U'):
            char = char.replace(char, '')
        new_string += char
    return new_string


if __name__ == "__main__":
    main()
