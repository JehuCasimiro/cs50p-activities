def main():
    camel_case = input("camelCase: ")
    new_string = snake_case(camel_case)
    print("snake_case:", new_string)

def snake_case(camel_case):
    new_string = ""
    for char in camel_case:
        if char.isupper():
            char = "_" + char.lower()
        new_string += char
    return new_string

main()