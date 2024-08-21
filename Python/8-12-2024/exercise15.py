#Sum of n natural numbers

def get_user_input() -> int:
    while True:
        try:
            num = int(input("Pick a positive integer.\nA: "))
            if num > 0:
                return num
            print("\nThis number isn't positive. Try again.")
        except ValueError:
            print("\nThat is not an integer. Try again.")

n = get_user_input()
print(f"The sum of every natural number until {n} is equal to {int(((1+n)*n)/2)}")