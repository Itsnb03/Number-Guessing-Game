import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to Guess the Number Game!")
    print("I've selected a number between 1 and 100. Can you guess it?")

    while True:
        user_guess = int(input("Your guess: "))
        attempts += 1

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    guess_the_number()