#List iteration

def get_limit() -> int:
    while True:
        try:
            limit = int(input("How many number would you like to add?\n[Pick a positive integer].\nA: "))
            if limit < 1:
                print("\nThis integer isn't positive. Try again.\n")
        except ValueError:
            print("\nThat's not an integer. Try again.\n")
        if limit < 11 and limit > 0:
            return limit
        elif limit > 11:
            print("\nThat's way too much. Pick a smaller amont.\n")
    
def get_numbers(limit: int) -> list:
    while True:
        try:
            nums = [float(input("\nPick a number.\nA: ")) for x in range(limit)]
        except ValueError:
            print("\nThat's not a number. Try Again.\n")
        return nums

def get_higher(numbers: list) -> float:
    L = 0; R = len(numbers) - 1; higher = numbers[0]
    while L < R:
        higher = numbers[L] if numbers[L] > higher else higher
        higher = numbers[R] if numbers[R] > higher else higher
        L += 1; R-= 1
    if L == R and numbers[L] > higher:
        higher = numbers[L]
    return higher

def get_lower(numbers: list) -> float:
    L = 0; R = len(numbers) - 1; lower = numbers[0]
    while L < R:
        lower = numbers[L] if numbers[L] < lower else lower
        lower = numbers[R] if numbers[R] < lower else lower
        L += 1; R-= 1
    if L == R and numbers[L] < lower:
        lower = numbers[L]
    return lower

def mean(numbers: list) -> float:
    L = 0; R = len(numbers) - 1; sum = 0
    while L < R:
        sum += numbers[L] + numbers[R]
        L += 1; R -= 1
    if L == R:
        sum += numbers[L]
    return sum / len(numbers)

def main():
    limit = get_limit()
    numbers = get_numbers(limit)
    print(f"\nWithin all the number you chose, the higher one was {get_higher(numbers)}", end=", ")
    print(f"the lower one was {get_lower(numbers)}", end=", ")
    print(f"and the mean of all the numbers was {mean(numbers)}")

main()