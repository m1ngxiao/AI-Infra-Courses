def main():
    emotion = input()
    print(faces(emotion))

def faces(emotion):
    return emotion.replace(":)", "🙂").replace(":(", "🙁")

main()