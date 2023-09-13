from validator_collection import checkers

def main():
    email = input("What's your email: ")
    result = "Valid" if checkers.is_email(email) else "Invalid"
    print(result)

if __name__ == "__main__":
    main()
