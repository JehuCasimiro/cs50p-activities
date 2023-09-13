import re

def main():
    print(count(input("Text: ")))


def count(s):
    total_um = re.findall(r"\b(um)\b", s, re.IGNORECASE)
    return len(total_um)


if __name__ == "__main__":
    main()