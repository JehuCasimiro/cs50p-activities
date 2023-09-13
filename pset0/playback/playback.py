def main():
    string = input("")
    newString = playback(string)
    print(newString)

def playback(str):
    return str.replace(" ", "...")

main()