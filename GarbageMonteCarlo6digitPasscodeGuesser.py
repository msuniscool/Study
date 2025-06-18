import random
import time

def monte_carlo_guess(target_code):
    attempts = 0
    start_time = time.time()

    while True:
        guess = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        attempts += 1
        if guess == target_code:
            break

    end_time = time.time()
    duration = end_time - start_time
    return attempts, duration

def main():
    # Get user input and validate it
    while True:
        user_code = input("Enter a 6-digit code (numbers only): ")
        if user_code.isdigit() and len(user_code) == 6:
            break
        else:
            print("Invalid input. Please enter exactly 6 digits.")

    attempts, duration = monte_carlo_guess(user_code)

    print(f"Correct code guessed: {user_code}")
    print(f"Number of attempts: {attempts}")
    print(f"Time taken: {duration:.4f} seconds")

if __name__ == "__main__":
    main()
