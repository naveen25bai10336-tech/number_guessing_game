import random

def guess_the_number():
    """
    A simple Number Guessing Game.
    The computer picks a random number, and the user tries to guess it.
    """
    
    # 1. Setup: Define the range and pick the number
    lower_bound = 1
    upper_bound = 50
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    
    print("--- Number Guessing Game ---")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    
    # 2. Game Loop
    while True:
        try:
            # Get user input
            guess = int(input("Enter your guess: "))
            attempts += 1
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue # Skip the rest of the loop and ask again

        # Check the guess
        if guess < lower_bound or guess > upper_bound:
            print(f"Your guess is outside the range ({lower_bound}-{upper_bound}). Try again.")
        elif guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            # Correct Guess - Exit the loop
            print(f"\n🎉 Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
            break

# Run the game
if __name__ == "__main__":
    guess_the_number()