#Print the multiplication number of an integer

while True:
    try:
        num = int(input("Pick a integer number.\nA: "))
        for x in range(1,11):
            print(f"{num} x {x} = {num*x}") 
        break
    except ValueError:
        print(f"\nThat's not an integer. Try again.")
