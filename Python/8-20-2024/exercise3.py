import random, time

def get_user_nums():
    num_pool = list(range(1,76))
    user_nums = []
    for _ in range(5):
        choice = random.choice(num_pool)
        user_nums.append(choice)
        num_pool.remove(choice)
    return user_nums

def main():
    user_nums = get_user_nums()
    round = 0
    num_pool = list(range(1,76))
    while len(user_nums) > 0:
        round += 1
        print(f"\nRound number {round}\n")
        print(f"The numbers in your card are: {user_nums}")
        time.sleep(2)
        choice = random.choice(num_pool)
        print(f"The number drawn was {choice}.")
        time.sleep(1)
        if choice in user_nums:
            print(f"\nThe number WAS in your bingo card!")
            user_nums.remove(choice)
            time.sleep(2)
        num_pool.remove(choice)
    print(f"\nGame Over! You finished your card in {round} rounds.")

main()
        
