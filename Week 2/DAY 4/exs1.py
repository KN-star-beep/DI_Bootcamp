import random

# Step 1: Read words from file
def get_words_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            words = content.split()
            return words
    except FileNotFoundError:
        print("Error: File not found.")
        return []
    # Step 2: Generate random sentence
def get_random_sentence(length):
    words = get_words_from_file("words.txt")
    
    if not words:
        return "No words available."
    
    sentence_words = []
    
    for _ in range(length):
        word = random.choice(words)
        sentence_words.append(word)
    
    sentence = " ".join(sentence_words).lower()
    return sentence
# Step 3: Main function
def main():
    print("Welcome! This program generates a random sentence.")
    
    user_input = input("Enter sentence length (2–20): ")
    
    # Input validation
    try:
        length = int(user_input)
        
        if length < 2 or length > 20:
            print("Error: Please enter a number between 2 and 20.")
            return
        
    except ValueError:
        print("Error: Please enter a valid integer.")
        return
    
    # Generate and print sentence
    sentence = get_random_sentence(length)
    print("Generated sentence:")
    print(sentence)


# Run the program
main()
