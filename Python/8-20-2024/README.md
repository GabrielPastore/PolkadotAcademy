# Python Exercises #4

## Exercise 1

The way the code works is by creating 2 core functions to the code, one wich will get the 2 integers needed to have the range for the iteration process and the one to properly iterate over the range chosen by the user. (Note that the first function already has exception & errors treatment through the use of try/except and conditionals to guarantee the user's input WILL be 2 positive integers.)

>try:
>    start = int(input("Pick a positive integer.\nA: "))
>    end = int(input("Pick another positive integer.\nA: "))
>    if start > -1 and end > -1:
>        if start != end:
>            return [start, end] if start < end else [end, start]
>        print("\nThe 2 numbers you chose were equal to each other. Try again.\n")
>    else:
>        print("\nOne of the 2 numbers you chose were not positive. Try again.\n")
>except ValueError:
>    print("\nThat's not an integer. Try Again.\n")

The function 'find_secret_number' works by iterating over the range given by the user through the Two Pointers Technique to optimize the run time of the code for instances where the user might want to verify over bigger ranges. This works by having one pointer (L) starting the iteration on the lower end of the range and one pointer (R) starting on the higher end. The solution will not fail if the user type the bigger number before the lower one because the 'get_numbers' function will return by standard the lower number first as seen below:

> return [start, end] if start < end else [end, start]

'find_secret_number' will always be faster in execution time because it iterates twice as fast. The numbers in the range will go under a verification to determine if it should be added or subtracted from the final answer. The way chosen to code this was by adding the number to a "sum" variable if at the same time being divisible by 3 and not by 5 and subtracting it from "sum" if divisible by 5 and not by 3. Doing this will remove the need to have a third verification for being divisible by 3 and 5 at the same time because a number will ONLY be read as correct if ONLY divisible by 3 OR 5.

>sum += L if L % 3 == 0 and L % 5 != 0 else 0; sum += R if R % 3 == 0 and R % 5 != 0 else 0
>sum -= L if L % 5 == 0 and L % 3 != 0 else 0; sum -= R if R % 5 == 0 and R % 3 != 0 else 0

At the end of this function, the code will return the 'sum' variable and present it to the user as the end of the program at the 'main' function.

## Exercise 2

The second exercise was not included here because it contains a logical fallacy on the initial statement. The proposal was to iterate over a integer range chosen by the user and return the first number to pass under the 3 verifications below:

> Be divisible by 4 | Be a prime number | To have the sum of the number's digits to add up to an odd number

Since the definition of a prime number is a number that only haves 2 divisors: 1 and itself, it's impossible to have a prime number divisible by 4 because it would mean the number would have AT LEAST 4 divisors (1, 2, 4 and itself) therefore not being a prime number anymore.

## Exercise 3

The solution to this exercise starts with the creation of the 'get_user_nums' function to pick all 5 numbers to the card. First the code creates a list of all the naturals from 1 to 75 to serve as the object being iterated over on the 'random.choice' function. The choice to use 'random.choice' on a list instead of 'random.randint' on a range was because by using the list object, it was possible to the remove the chosen number from the list to prevent it being the next chosen number on the next iteration. By doing this, the code will never have a repeated number on the user's card. The function returns the 5 chosen numbers inside a list at the end of the for loop as seen below:

>num_pool = list(range(1,76))
>    user_nums = []
>    for _ in range(5):
>        choice = random.choice(num_pool)
>        user_nums.append(choice)
>        num_pool.remove(choice)
>    return user_nums

The 'main' function works on a very similar way to 'get_user_nums'. It will have a variable called 'round' to count the amount of rounds the program took to finish. The function has a while loop that will run until the 'user_nums' list (assigned from the previous function) has a length of 0 elements. At the start of each iteration of the loop, 'round' will have 1 added to indicate a new round of the game then the 'random.choice' function will choose a random number through the same technique previously noted. If the chosen number is one of the elements of the list 'user_nums', this number will be erased from this list. The chosen number will be removed from the 'nums_pool' even if it's not in the user's list to prevent the code to choose a number twice, this will limit the max amount of rounds the game could take to run to the length of the naturals range (in this case it is 75). The 'time.sleep' function is utilized to make the program looks more like a bingo game instead of executing all the iterations on an almost-instantantenous time. 

>user_nums = get_user_nums()
>    round = 0
>    num_pool = list(range(1,76))
>    while len(user_nums) > 0:
>        round += 1
>        print(f"\nRound number {round}\n")
>        print(f"The numbers in your card are: {user_nums}")
>        time.sleep(2)
>        choice = random.choice(num_pool)
>        print(f"The number drawn was {choice}.")
>        time.sleep(1)
>        if choice in user_nums:
>            print(f"\nThe number WAS in your bingo card!")
>            user_nums.remove(choice)
>            time.sleep(2)
>        num_pool.remove(choice)
>    print(f"\nGame Over! You finished your card in {round} rounds.")

When all 5 elements of the 'user_nums' list are erased, the while loop will break and print to the user the game is finished alongside with the amount of rounds the needed to complete the bingo.