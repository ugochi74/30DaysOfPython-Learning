# 1. Create your user-defined function
def format_name(dirty_name):
    # STEP 1: Strip the whitespace
    word = dirty_name.split()
    
    # STEP 2: Convert to Title Case (Hint: use the .title() method)
    cleaned_name = " ".join(word)
    cleaned_name = cleaned_name.title()
    
    # STEP 3: Use a built-in function to count the length of the cleaned name
    name_length = len(cleaned_name)
    
    # Return the final cleaned name
    print("The cleaned name", name_length, "Characters.")
    return cleaned_name

# 2. Test your function with this messy input
test_name = "   jAnE   dOe   "
result = format_name(test_name)

print("Final Output:", result)
# Expected Final Output: "Jane Doe"
