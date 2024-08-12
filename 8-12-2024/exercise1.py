#Calculate the factorial of a user-given number

def factorial(x: int) -> int:
    if x == 1 or 0:
        return 1
    return x * factorial(x-1)

while True: #We can't have 
    num = int(input("Pick a non negative integer number.\nA: "))
    if num > 0:
        break

print(f"The factorial of {num} is equal to {factorial(num)}")