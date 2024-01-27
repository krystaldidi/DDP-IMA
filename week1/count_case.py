def case_counter(text):
    # Initialize counts for uppercase and lowercase letters
    uppercase_count = 0
    lowercase_count = 0

    # Iterate through each character in the string
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            uppercase_count += 1
        # Check if the character is a lowercase letter
        elif char.islower():
            lowercase_count += 1

    # Return the counts of uppercase and lowercase letters
    return uppercase_count, lowercase_count

# Test cases
print(case_counter("Hello World!"))  # Expected: (Uppercase letters: 2, Lowercase letters: 8)
print(case_counter("PYTHON"))  # Expected: (Uppercase letters: 6, Lowercase letters: 0)
print(case_counter("python"))  # Expected: (Uppercase letters: 0, Lowercase letters: 6)
print(case_counter("1234!@#$"))  # Expected: (Uppercase letters: 0, Lowercase letters: 0)
