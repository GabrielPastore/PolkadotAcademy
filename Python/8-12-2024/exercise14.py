#Simple calculator

add = lambda a, b: a + b
reduce = lambda a, b: a - b
mult = lambda a, b: a * b
div = lambda a, b: a / b

operations = {"+": add, "-": reduce, "*": mult, "/": div}

while True:
    try:
        nums = [int(input("Pick a number.\nA: ")) for x in range(2)]
        break
    except ValueError:
        print("\nThat is not a number. Try again.")

print("\nNow choose what operation you want those numbers to go through")
print("['+' for Addition, '-' for Subtraction, '*' for Multiplication and '/' for Division]")
operator = input("A: ")
while operator not in operations:
    print("\nUnable to do the calculations. You sent an invalid operator. Try Again.")
    print("['+' for Addition, '-' for Subtraction, '*' for Multiplication and '/' for Division]")
    operator = input("\nA: ")
print(f"\nThe result of {nums[0]} {operator} {nums[1]} is {operations.get(operator)(nums[0], nums[1])}")