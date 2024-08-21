#Calculate the user's BMI

def bmi(height: float, weight: float) -> str:
    return str(weight / ((height/100)**2))[:5]

def main():
    while True:
        try:
            height = float(input(f"Say your height (in centimeters).\nA: "))
            weight = float(input(f"\nSay your wheight (in kilograms).\nA: "))
            if height > 0 and weight > 0:
                print(f"\nYour BMI is {bmi(height, weight)}")
                break
            print("\nYour height/weight can't be 0 or lower. Try again.\n")
        except ValueError:
            print("\nThat's not a number. Try again.\n")

main()