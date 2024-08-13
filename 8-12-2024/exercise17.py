#Check perfect number

def get_user_input() -> int:
    while True:
        try:
            num = int(input("Pick a positive integer.\nA: "))
            if num > 0:
                return num
            print("\nThis number isn't positive. Try again.")
        except ValueError:
            print("\nThat is not an integer. Try again.")

def check_divisors(x: int) -> list:
    L = 1; R = x-1
    divisors = list()
    while L < R:
        if x % L == 0:
            divisors.append(L)
        if x % R == 0:
            divisors.append(R)
        R -= 1; L += 1
    if L == R and x % L == 0:
        divisors.append(L)
    return divisors

def sum_divisors(x: list) -> int:
    L = 0; R = len(x) - 1; sum = 0
    while L < R:   
        sum += x[L]; sum += x[R]
        L += 1; R -= 1
    if L == R:
        sum += x[L]
    return sum

def main():
    choice = get_user_input()
    divisors = check_divisors(choice)
    divisors_sum = sum_divisors(divisors)
    print(f"{choice} is a perfect number.") if divisors_sum == choice else print(f"{choice} is not a perfect number")

main()