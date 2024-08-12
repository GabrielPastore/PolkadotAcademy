#Convert user-given temperature (in Celsius degrees) to Fahrenheit and Kelvin

while True:
    try:
        temp = float(input("Pick a temperature in Celsius degrees\nA: "))
        break
    except ValueError:
        print("\nThat's not a number. Try again.")

print(f"\nThe temperature of {temp}ºC is equivalent to:\n")
print(f"Fahrenheit: {(temp * 9)/5 + 32}ºF",f"Kelvin: {temp+213.15}K", sep="\n")