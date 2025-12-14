def main():
    x, y, z = input("Expression: ").split()
    result= interpreter(x, y, z)
    print(f"{result:.1f}")

def interpreter(x, y, z):
    x = float(x)
    z = float(z)
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z

main()