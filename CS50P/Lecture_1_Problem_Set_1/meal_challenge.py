def main():
    time = input("What time is it? ").strip().lower()
    result = convert(time)
    if result:
        print(result)

def convert(time):
    end = None
    if time.endswith("a.m."):
        end = "a.m."
        time = time[:-4]
    elif time.endswith("am"):
        end = "a.m."
        time = time[:-2]        
    elif time.endswith("p.m."):
        end = "p.m."
        time = time[:-4]
    elif time.endswith("pm"):
        end = "p.m."
        time = time[:-2]
    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute)
    if end == "a.m." and hour == 12:
        hour = 0
    elif end == "p.m." and hour != 12:
        hour += 12

    time = hour + minute / 60.0
    if 7 <= time <= 8:
        return "breakfast time"
    elif 12 <= time <= 13:
        return "lunch time"
    elif 18 <= time <= 19:
        return "dinner time"

if __name__ == "__main__":
    main()