import re

def main():
    print(convert(input("Hours: ")))

def convert(hour):
    match = re.search(r"^([1-9]|[1][0-2])(:[0-5][0-9])? (am|pm) to ([1-9]|[1][0-2])(:[0-5][0-9])? (am|pm)$",hour, re.IGNORECASE)
    if not match:
        raise ValueError
    value_1 = int(match.group(1)) % 12
    value_4 = int(match.group(4)) % 12
    start_minutes = match.group(2) or ":00"
    end_minutes = match.group(5) or ":00"
    if match.group(3).lower() == "pm":
        value_1 += 12
    if match.group(6).lower() == "pm":
        value_4 += 12
    return f"{value_1:02d}{start_minutes} to {value_4:02d}{end_minutes}"
if __name__ == "__main__":
    main()
