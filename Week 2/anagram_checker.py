class AnagramChecker:
    def __init__(self, file_path):
        try:
            with open(file_path, "r") as file:
                words = file.read().split()
                # Store words in lowercase for case-insensitive comparison
                self.word_list = set(word.lower() for word in words)
        except FileNotFoundError:
            print("Error: Word list file not found.")
            self.word_list = set()

    # Step 2: Check if word exists in dictionary
    def is_valid_word(self, word):
        return word.lower() in self.word_list

    # Step 3: Check if two words are anagrams
    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    # Step 4: Get all anagrams
    def get_anagrams(self, word):
        word = word.lower()
        anagrams = []

        for w in self.word_list:
            if w != word and self.is_anagram(word, w):
                anagrams.append(w)

        return anagrams