#Calculate the factorial of a user-given number

def factorial(x: int) -> int:
    if x == 1 or x == 0:
        return 1
    return x * factorial(x-1)
    
while True: #We can't have factorial of negative integers
    try:
        num = int(input("Pick a non negative integer number.\nA: "))
        if num > -1:
            break
        print("\nThis number is not positive. Try again.")
    except ValueError:
        print(f"\nThat's not an integer. Try again.")

print(f"The factorial of {num} is equal to {factorial(num)}")