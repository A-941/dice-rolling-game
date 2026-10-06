import random

while True:
    answer = input("Do you want to roll the dice? (y/n): ").strip().lower()

    if answer == 'y':
        result = random.randint(1, 6)
        print(f"You rolled: {result}")
    elif answer == 'n':
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("Invalid input. Please enter y or n.")
