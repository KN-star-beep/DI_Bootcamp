from anagram_checker import AnagramChecker

def main():
    checker = AnagramChecker("wordlist.txt")  # Your word list file

    while True:
        print("\n--- Anagram Checker ---")
        print("Enter a word or type 'exit' to quit")

        user_input = input("Enter a word: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Step 3: Input validation
        if not user_input.isalpha():
            print("Error: Please enter a valid word (letters only).")
            continue

        # Step 4: Check validity
        is_valid = checker.is_valid_word(user_input)

        if not is_valid:
            print(f"'{user_input}' is NOT a valid word in the dictionary.")
            continue

        # Find anagrams
        anagrams = checker.get_anagrams(user_input)

        print(f"\nYour word: {user_input.lower()}")
        print("This is a valid English word.")

        if anagrams:
            print("Anagrams found:")
            print(", ".join(anagrams))
        else:
            print("No anagrams found.")


if __name__ == "__main__":
    main()
