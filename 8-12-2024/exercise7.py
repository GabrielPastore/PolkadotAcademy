#Arithmetic mean of a student's grades

def mean(grades: list) -> float:
    sum = 0
    L = 0
    R = len(grades) - 1
    while L < R:
        sum += grades[L] + grades[R]
        L += 1
        R -= 1
    if L == R:
        sum += grades[L]
    return sum / len(grades)

def main():
    grades_list = []
    while True:
        try:
            grade = float(input("\nSay your test's grade.\n[Type '-1' to stop adding grades]\nA: "))
            if grade == -1:
                break
            elif grade > -1:
                grades_list.append(grade)
            else:
                print("\nNegative grades doesn't exist. Try again.\n")
        except ValueError:
            print("\nThat's not a number. Try again.\n")
    print(f"Your average score was {mean(grades_list)}") if grades_list is not [] else print("You didn't give any grades.")

main()