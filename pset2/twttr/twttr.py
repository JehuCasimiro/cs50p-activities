def main():
    string = input("Input: ")
    new_string = twttr(string)
    print("Output:", new_string)

def twttr(s):
    new_string = ""
    for c in s:
        if (c == 'a' or c == 'e' or c == 'i' or
        c == 'o' or c == 'u' or c == 'A' or
        c == 'E' or c == 'I' or c == 'O' or
        c == 'U'):
            c = c.replace(c, '')
        new_string += c
    return new_string

main()
