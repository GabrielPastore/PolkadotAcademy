#Guessing random numbers
from random import randint

def get_user_input() -> int:
    while True:
        try:
            num = int(input("Pick a positive integer.\nA: "))
            if num > 0 and num < 100:
                return num
            elif num < 1:    
                print("\nThis number isn't positive. Try again.")
            elif num > 100:
                print("\nThis number is too high, pick one between 1-100. Try again.")
        except ValueError:
            print("\nThat is not an integer. Try again.")

def main():
    target = randint(1,100)
    round = 0
    print("In this game, your objective is to guess the number the CPU chose.")
    print("After each guess, the computer will tell you if your number is higher or lower than the correct number.")
    print("The number to be found will be in a range of 1-100.\n")
    print("Good Luck!")
    while True:
        print("\n----- Your Turn -----\n")
        choice = get_user_input()
        round += 1
        if choice == target:
            break
        elif choice > target:
            print(f"\nYour number ({choice}) is greater than the CPU number!")
        else:
            print(f"\nYour number ({choice}) is lower than the CPU number!")
    print("\nCongratulations! You Won!!!")
    print(f"It took you {choice} rounds to guess the correct number")

main()