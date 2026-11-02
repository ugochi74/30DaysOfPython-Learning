class Solution:
    def romanToInt(self, s: str) -> int:
        # Map each Roman symbol to its integer value
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        length = len(s)
        
        for i in range(length):
            current_value = roman_map[s[i]]
            
            # If the current value is less than the next value, subtract it
            if i + 1 < length and current_value < roman_map[s[i+1]]:
                total -= current_value
            # Otherwise, add it to the running total
            else:
                total += current_value
                
        return total