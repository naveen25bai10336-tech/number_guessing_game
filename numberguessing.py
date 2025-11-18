import random

def start_game():
    """
    A simple Number Guessing Game.
    The computer picks a random number, and the user tries to guess it.
    """
    
    # 1.here i have mentioned the conditions 
    minimum_value = 1
    maximum_value = 50
    target_num = random.randint(minimum_value, maximum_value)
    guess_counts = 0
    
    print("--- Number Guessing Game ---")
    print(f"I'm thinking of a number between {minimum_value} and { maximum_value}.")
    
    # 2. loops starts here
    while True:
        try:
            # here i wll enter input 
            guess = int(input("enter number : "))
            attempts += 1
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue # Skip the rest of the loop and ask again

        # check the input
        if guess < minimum_value or guess >  maximum_value:
            print(f"Your guess is outside the range ({minimum_value}-{ maximum_value}). Try again.")
        elif guess < target_num:
            print("Too low! Try again.")
        elif guess > target_num:
            print("Too high! Try again.")
        else:
            # Correct input - Exit the loop
            print(f"\n🎉 Congratulations! You guessed the number {target_num} correctly in {attempts} attempts.")
            break

# Run the game
if __name__ == "__main__":
   start_game()




