#Weighted arithmetic mean

def get_grades() -> dict:
    grades_list = []
    weights = [2, 3, 5]
    while True:
        try:
            grade = float(input("\nSay your test's grade.\nA: "))
            if grade > -1:
                grades_list.append(grade)
            else:
                print("\nNegative grades doesn't exist. Try again.\n")
        except ValueError:
            print("\nThat's not a number. Try again.\n")
        if len(grades_list) >= 3:
                return {grades_list[x]: weights[x] for x in range(3)}
        
def get_mean(x: dict) -> float:
    up_result = 0; down_result = 0
    for k, v in x.items():
        up_result += (k * v); down_result += v
    return up_result / down_result

def main():
    grades = get_grades()
    mean = get_mean(grades)
    print(f"\nYour average score was {mean}")
    
main()