#Invert a string
def str_inverter(x: str) -> str:
    return x[::-1]

string = input("Write a sentence.\nA: ")
print(f"\nIts inverted form is: {str_inverter(string)}")