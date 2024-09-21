import random

def guess_the_number():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        try:
            # Prompt the user to enter their guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Compare the guess with the random number
            if user_guess < random_number:
                print("Too low! Try again.")
            elif user_guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
