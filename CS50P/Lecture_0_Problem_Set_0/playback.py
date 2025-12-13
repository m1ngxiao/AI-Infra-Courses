def main():
    speed = input()
    print(playback(speed))

def playback(speed):
    return speed.replace(" ", "...")

main()