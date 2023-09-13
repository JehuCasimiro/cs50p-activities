def main():
    answer = input("What is the Answer to the Grade Question of Life, the Universe, and Everything? ")
    print(deep(answer))

def deep(answer):
    newAnswer = answer.lower().strip()

    if newAnswer == "42":
        return "Yes"
    elif newAnswer == "forty-two":
        return "Yes"
    elif newAnswer == "forty two":
        return "Yes"
    else:
        return "No"

main()