import random

def number_guessing_game():
    # Generate a random number between 1 and 10
    random_number = random.randint(1, 10)
    attempts = 0
    max_attempts = 3  # You can customize the number of attempts allowed

    print("Welcome to the Number Guessing Game!")
    print(f"Try to guess the number between 1 and 10. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            # Get user input for the guess
            user_guess = int(input("Enter your guess: "))

            # Check if the guess is correct
            if user_guess == random_number:
                print(f"Congratulations! You guessed the correct number {random_number}!")
                break
            else:
                print("Incorrect guess. Try again.")
                attempts += 1

            # Provide a hint if the user has more attempts
            if attempts < max_attempts:
                print("Here's a hint: The number is higher." if user_guess < random_number
                      else "Here's a hint: The number is lower.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {random_number}.")

# Example usage:
if __name__ == "__main__":
    number_guessing_game()
