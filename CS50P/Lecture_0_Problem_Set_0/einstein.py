def main():
    n = int(input("m: "))
    E = einstein(n)
    print("E:", E)

def einstein(n):
    return n * 300000000**2

main()
