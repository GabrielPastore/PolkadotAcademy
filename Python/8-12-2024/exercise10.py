#Say if a number is odd or even

while True:
    try:
        n = int(input("Pick a integer.\nA: "))
        break
    except ValueError:
        print("\nThat's not an integer. Try Again.\n")

print("\nYour number is odd" * (n % 2 == 1), "\nYour number is even" * (n % 2 == 0), sep="")