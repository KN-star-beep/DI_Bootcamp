import random

class Game:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]

    # Step 2: User choice
    def get_user_item(self):
        while True:
            user_input = input("Choose rock, paper, or scissors: ").lower().strip()
            if user_input in self.choices:
                return user_input
            print("Invalid choice. Try again.")

    # Step 3: Computer choice
    def get_computer_item(self):
        return random.choice(self.choices)

    # Step 4: Determine result
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"

        if (
            (user_item == "rock" and computer_item == "scissors") or
            (user_item == "scissors" and computer_item == "paper") or
            (user_item == "paper" and computer_item == "rock")
        ):
            return "win"

        return "loss"

    # Step 5: Play game
    def play(self):
        user = self.get_user_item()
        computer = self.get_computer_item()

        result = self.get_game_result(user, computer)

        print(f"\nYou chose: {user}")
        print(f"Computer chose: {computer}")
        print(f"Result: {result.upper()}\n")

        return result