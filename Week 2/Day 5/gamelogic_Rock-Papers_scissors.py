from game import Game

# Step 6: Menu
def get_user_menu_choice():
    print("\n--- Rock Paper Scissors ---")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")

    while True:
        choice = input("Enter your choice (1-3): ").strip()

        if choice in ["1", "2", "3"]:
            return choice

        print("Invalid input. Please enter 1, 2, or 3.")

# Step 7: Print results
def print_results(results):
    print("\n--- Game Summary ---")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("\nThanks for playing! 🎮")

# Step 8: Main function
def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    game = Game()

    while True:
        choice = get_user_menu_choice()

        if choice == "1":
            result = game.play()
            results[result] += 1

        elif choice == "2":
            print_results(results)

        elif choice == "3":
            print_results(results)
            break


if __name__ == "__main__":
    main()