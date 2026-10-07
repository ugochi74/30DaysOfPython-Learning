def break_words(stuff):
 """This function will break up words for us."""
 words = stuff.split(' ')
 return words

def sort_words(words):
 """Sorts the words."""
 return sorted(words)

def print_first_word(words):
 """Prints the first word after popping it off."""
 word = words.pop(0)
 print (word)

def print_last_word(words):
 """Prints the last word after popping it off."""
 word = words.pop(- 1)
 print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
   """Prints the first and last words of the sentence."""
   words = break_words(sentence)
   print_first_word(words)
   print_last_word(words)
def print_first_and_last_sorted(sentence):
   """Sorts the words then prints the first and last one."""
   words = sort_sentence(sentence)
   print_first_word(words)
   print_last_word(words)

if __name__ == "__main__":
    print("--- STARTING TESTS ---")
    
    # 1. Define a sample sentence
    test_sentence = "All good things come to those who wait"
    
    # 2. Test break_words()
    print("\nTesting break_words...")
    words = break_words(test_sentence)
    assert words == ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait'], " break_words failed!"
    print(" break_words passed.")
    
    # 3. Test sort_words()
    print("\nTesting sort_words...")
    sorted_words = sort_words(words)
    assert sorted_words == ['All', 'come', 'good', 'things', 'those', 'to', 'wait', 'who'], "❌sort_words failed!"
    print("sort_words passed.")
    
    # 4. Test print_first_and_last()
    print("\nTesting print_first_and_last...")
    print("[Expected output below: All, then wait]")
    print_first_and_last(test_sentence)
    
    # 5. Test print_first_and_last_sorted()
    print("\nTesting print_first_and_last_sorted")
    print("[Expected output below: All, then who]")
    print_first_and_last_sorted(test_sentence)
    
    print("\n ALL FUNCTIONS ARE WORKING PERFECTLY WELL! ")