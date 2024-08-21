#Calculate the area of a circle (considering Pi to be 3.14)

while True:
    try:
        radius = int(input("Pick a positive integer.\nA: "))
        if radius > 0:
            break
        print("\nThis number isn't positive. Try again.")
    except ValueError:
        print("\nThat is not an integer. Try again.")
print(f"The area of the circle made by a radius of your integer is {3.14 * (radius**2)} cm².")