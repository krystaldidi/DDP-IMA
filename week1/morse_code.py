def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    # Convert the input text to uppercase for case-insensitivity
    text = text.upper()

    # List to store the translated Morse code for each character
    morse_code_list = []

    # Iterate through each character in the input text
    for char in text:
        # Check if the character is an alphabetic character
        if char.isalpha():
            # Translate the character to Morse code and append to the list
            morse_code_list.append(morse_code_dict[char])
        elif char.isspace():
            # For space, add a slash (/) to separate words
            morse_code_list.append("/")
    
    # Join the Morse code elements with spaces and return the result
    return " ".join(morse_code_list)

# Test cases
print(morse_translator("HELLO WORLD"))  # Expected output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
print(morse_translator("Python"))  # Expected output: ".--. -.-- - .... --- -."
print(morse_translator("Morse Code"))  # Expected output: "-- --- .-. ... . / -.-. --- -.. ."
