import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A|P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A|P]M)$", s):
        parts = matches.groups()
        if int(parts[1]) > 12 or int(parts[5]) > 12:
            raise ValueError
        
        new_time_1 = format(parts[1], parts[2], parts[3])
        new_time_2 = format(parts[5], parts[6], parts[7])
        return f"{new_time_1} to {new_time_2}"
    else:
        raise ValueError

def format(hh, mm, format):
    if format == "AM":
        if int(hh) == 12:
            new_hh = 0
        else:
            new_hh = int(hh)
    else:
        if int(hh) == 12:
            new_hh = 12
        else:
            new_hh = int(hh) + 12

    if mm == None:
        new_mm = ":00"
        new_time = f"{new_hh:02}"  + new_mm
    else:
        new_time = f"{new_hh:02}" + ":" + mm

    return new_time

if __name__ == "__main__":
    main()