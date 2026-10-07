def get_word_count(text):
    """Returns the total number of words in a text."""
    words = text.split(' ')
    return len(words)

def find_longest_word(text):
    """Finds and returns the longest word in the string."""
    words = text.split(' ')
    # sorted() can sort by word length if we use key=len
    sorted_by_length = sorted(words, key=len)
    return sorted_by_length[-1]  # The last item will be the longest

def generate_secret_code(text):
    """Takes the first letter of each word to create a secret acronym."""
    words = text.split(' ')
    code = ""
    for word in words:
        if word:  # Make sure the word isn't empty spaces
            code += word[0].upper()
    return code

# --- Test Block ---
if __name__ == "__main__":
    print("--- Text Analyzer Script ---")
    sample = "Python is an amazing language to learn for automation"
    
    print(f"Analyzing: '{sample}'")
    print(f"Total Words: {get_word_count(sample)}")
    print(f"Longest Word: {find_longest_word(sample)}")
    print(f"Secret Code: {generate_secret_code(sample)}")
