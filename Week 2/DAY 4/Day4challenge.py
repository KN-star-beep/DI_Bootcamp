import re
import string

class Text:
    def __init__(self, text):
        self.text = text.lower()

    # Step 2: Word frequency
    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word.lower())
        
        if count == 0:
            return f"The word '{word}' was not found."
        
        return count

    # Step 3: Most common word
    def most_common_word(self):
        words = self.text.split()
        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        most_common = max(freq, key=freq.get)
        return most_common

    # Step 4: Unique words
    def unique_words(self):
        words = self.text.split()
        unique = set(words)
        return list(unique)

    # Step 5: Create from file
    @classmethod
    def from_file(cls, file_path):
        try:
            with open(file_path, "r") as file:
                content = file.read()
                return cls(content)
        except FileNotFoundError:
            print("File not found.")
            return None
        class TextModification(Text):

    # Step 7: Remove punctuation
    def remove_punctuation(self):
        no_punct = self.text.translate(str.maketrans("", "", string.punctuation))
        return no_punct

    # Step 8: Remove stop words
    def remove_stop_words(self):
        stop_words = {
            "a", "an", "the", "is", "in", "on", "and", "or", "of", "to", "for",
            "with", "without", "at", "by", "from", "as", "it", "this", "that"
        }

        words = self.text.split()
        filtered = [word for word in words if word not in stop_words]

        return " ".join(filtered)

    # Step 9: Remove special characters
    def remove_special_characters(self):
        cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", self.text)
        return cleaned
    # Create object
text = Text("Hello hello world! This is a simple test. Hello world.")

# Word frequency
print(text.word_frequency("hello"))

# Most common word
print("Most common word:", text.most_common_word())

# Unique words
print("Unique words:", text.unique_words())

# From file (if you have a file.txt)
# text_from_file = Text.from_file("file.txt")

# Text modification
mod_text = TextModification("Hello!!! This is, a test. Testing, one, two, three.")

print("No punctuation:", mod_text.remove_punctuation())
print("No stop words:", mod_text.remove_stop_words())
print("No special characters:", mod_text.remove_special_characters())