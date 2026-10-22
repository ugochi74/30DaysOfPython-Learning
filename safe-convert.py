def safe_convert_to_int(user_input):
    """Safely convert a string to an integer, handling ValueError."""
    try:
        value = int(user_input)
        print(f"Successfully converted to: {value}")
        return value
    except ValueError:
        print(f"Error: '{user_input}' is not a valid integer")
        return None


# Test the function
safe_convert_to_int("25")          
safe_convert_to_int("3.14")         
safe_convert_to_int("hello")      
safe_convert_to_int("")             
safe_convert_to_int("  42  ")      