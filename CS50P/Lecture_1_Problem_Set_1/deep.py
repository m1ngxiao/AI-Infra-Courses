def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    print(deep(answer))

def deep(answer):
    if answer in ["42", "forty-two", "forty two"]:
        return "Yes"
    else:
        return "No"

main()
