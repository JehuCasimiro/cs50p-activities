import requests
import sys

def main():
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")
        elif float(sys.argv[1]):
            try:
                response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
                rate = float(response.json()["bpi"]["USD"]["rate"].replace(",", ""))
                user_input = float(sys.argv[1])
                amount = rate * user_input

                print(f"${amount:,.4f}")

            except requests.RequestException:
                print("error")
    except ValueError:
        sys.exit("Command-line argument is not a number")

if __name__ == "__main__":
    main()