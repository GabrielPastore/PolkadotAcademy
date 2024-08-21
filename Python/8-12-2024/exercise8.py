#Fibonacci

def fibo(x: int) -> int:
    if x <= 1:
        return x
    return (fibo(x-1) + fibo(x-2))

def main():
    while True:
        try:
            index = int(input("Pick a positive integer.\nA: "))
            if index < 1:
                print("\nThis integer isn't positive. Try again.")
            else:
                break
        except ValueError:
            print("\nThat's not an integer. Try again.")
    print(f"\nThe Fibonacci sequence until the {index}th number is:")
    print(*[fibo(x) for x in range(index)], sep=", ")

main()