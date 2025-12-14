def main():
    time = input("What time is it? ")
    result = convert(time)
    if result:
        print(result)

def convert(time):
    hour, minute = time.split(":")
    time = float(hour) + float(minute) / 60
    if 7 <= time <= 8:
        return "breakfast time"
    elif 12 <= time <= 13:
        return "lunch time"
    elif 18 <= time <= 19:
        return "dinner time"

if __name__ == "__main__":
    main()