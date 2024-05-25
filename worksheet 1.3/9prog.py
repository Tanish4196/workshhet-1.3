def check_character_type(char):
    if char.isdigit():
        return "Digit"
    elif char.isalpha():
        return "Alphabet"
    else:
        return "Special character"

char = input("Enter a character: ")

if len(char) == 1:
    result = check_character_type(char)
    print(result)
else:
    print("Invalid input! Please enter a single character.")
