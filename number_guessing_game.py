"""
========================================
Number Guessing Game
Author  : Anselm Munango
Purpose : Generate a random integer between 1 and 100 and challenge the
          user to identify it within a fixed number of attempts, providing
          directional feedback after each incorrect guess.
========================================
"""

import random

# ------------------------------------------
# Game configuration constants
# ------------------------------------------

LOWER_BOUND: int = 1
UPPER_BOUND: int = 100
MAX_ATTEMPTS: int = 7


# ------------------------------------------
# Input helper
# ------------------------------------------

def get_integer_guess(prompt: str, low: int, high: int) -> int:
    """
    Prompt the user for an integer within [low, high], re-prompting on
    invalid or out-of-range input.

    Args:
        prompt (str): The message displayed to the user.
        low    (int): Minimum acceptable value (inclusive).
        high   (int): Maximum acceptable value (inclusive).

    Returns:
        int: A validated integer within the specified range.
    """
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            print(f"  Please enter a number between {low} and {high}.\n")
        except ValueError:
            print("  Invalid input. Please enter a whole number.\n")


# ------------------------------------------
# Core game logic
# ------------------------------------------

def play_round() -> bool:
    """
    Execute a single round of the guessing game.

    Returns:
        bool: True if the player guessed correctly; False if attempts exhausted.
    """
    secret = random.randint(LOWER_BOUND, UPPER_BOUND)

    print(f"\n  A number between {LOWER_BOUND} and {UPPER_BOUND} has been selected.")
    print(f"  You have {MAX_ATTEMPTS} attempts. Good luck!\n")

    for attempt_number in range(1, MAX_ATTEMPTS + 1):
        remaining = MAX_ATTEMPTS - attempt_number + 1
        prompt = (
            f"  Attempt {attempt_number}/{MAX_ATTEMPTS} "
            f"({remaining} remaining) - Your guess: "
        )
        guess = get_integer_guess(prompt, LOWER_BOUND, UPPER_BOUND)

        if guess == secret:
            print(
                f"\n  Correct! The number was {secret}. "
                f"You solved it in {attempt_number} attempt(s)!"
            )
            return True
        elif guess < secret:
            print("  Too low - try a higher number.\n")
        else:
            print("  Too high - try a lower number.\n")

    print(f"\n  Out of attempts. The secret number was {secret}.")
    return False


# ------------------------------------------
# Main application loop
# ------------------------------------------

def run_game() -> None:
    """
    Manage the game session, tracking wins and losses across multiple rounds
    until the player chooses to quit.
    """
    wins   = 0
    losses = 0

    print("\n" + "=" * 46)
    print("    WELCOME TO THE NUMBER GUESSING GAME")
    print("=" * 46)

    while True:
        if play_round():
            wins += 1
        else:
            losses += 1

        print(f"\n  Session score - Wins: {wins}  |  Losses: {losses}")
        again = input("\n  Would you like to play again? (yes / no): ").strip().lower()

        if again not in ("yes", "y"):
            print(
                f"\n  Thanks for playing! Final score - "
                f"Wins: {wins}, Losses: {losses}. See you next time!\n"
            )
            break


# ------------------------------------------
# Entry point
# ------------------------------------------

if __name__ == "__main__":
    run_game()
