#Sum of every even number between 1-100

def sum_of_evens(start:int, target:int) -> int:
    L = int(start); R = int(target)
    sum = 0
    while L<R:
        if L % 2 == 0:
            sum += L
        if R % 2 == 0:
            sum += R
        L += 1; R -= 1
    if L == R and L % 2 == 0:
        sum += L
    return sum

print(f"The sum of every even number between 1-100 is {sum_of_evens(1,100)}")