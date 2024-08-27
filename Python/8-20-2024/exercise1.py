'''
Find a secret number hidden within the range of two positive integers. Criteria to find the number:
add the number to a sum if divisible by 3
subtract the number from the sum if divisible by 5
do not iterate if divisible by both 3 and 5 at the same time
'''

def get_numbers():
    while True:
        try:
            start = int(input("Pick a positive integer.\nA: "))
            end = int(input("Pick another positive integer.\nA: "))
            if start > -1 and end > -1:
                if start != end:
                    return [start, end] if start < end else [end, start]
                print("\nThe 2 numbers you chose were equal to each other. Try again.\n")
            else:
                print("\nOne of the 2 numbers you chose were not positive. Try again.\n")
        except ValueError:
            print("\nThat's not an integer. Try Again.\n")

def find_secret_number(lower: int, higher: int) -> int:
    L = lower; R = higher; sum = 0
    while L < R:
        sum += L if L % 3 == 0 and L % 5 != 0 else 0; sum += R if R % 3 == 0 and R % 5 != 0 else 0
        sum -= L if L % 5 == 0 and L % 3 != 0 else 0; sum -= R if R % 5 == 0 and R % 3 != 0 else 0
        L += 1; R -= 1
    if L == R:
        sum += L if L % 3 == 0 and L % 5 != 0 else 0
        sum -= L if L % 5 == 0 and L % 3 != 0 else 0
    return sum

def main():
    print(f"\nThe secret Polkadot number is: {find_secret_number(*get_numbers())}")

main()