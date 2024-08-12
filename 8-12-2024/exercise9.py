#Sort a list of N numbers

while True:
    try:
        nums = [float(input("Pick a number.\nA: ")) for x in range(3)]
        break
    except ValueError:
        print("\nThat's not a number. Try Again.\n")

nums.sort()
print(nums)