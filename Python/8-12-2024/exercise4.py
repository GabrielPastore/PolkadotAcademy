#Check if a string is a palindrome

def check_palindrome(x: str) -> bool:
    x = x.lower().replace(" ", "")
    return True if x == x[::-1] else False

if check_palindrome(input("Enter a sentence.\nA: ")):
    print("Your sentence is a palindrome.")
else:
    print("Your sentence is not a palindrome.")