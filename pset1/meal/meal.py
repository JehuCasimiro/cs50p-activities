def main():
    time_str = input("Enter the time in 24-hour format (hh:mm): ")
    time = convert(time_str)
    check_meal_time(time)

def convert(time):
    hours, minutes = time.split(":")
    time = float(hours) + float(minutes) / 60
    return time

def check_meal_time(time):
    if 7 <= time <= 8:
        print("breakfast time")
    if 12 <= time <= 13:
        print("lunch time")
    if 18 <= time <= 19:
        print("dinner time")

if __name__ == "__main__":
    main()
