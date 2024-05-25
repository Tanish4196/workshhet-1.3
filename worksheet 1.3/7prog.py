def check_vowel_or_consonant(char):
    vowels = 'aeiouAEIOU'
    if char in vowels:
        return "Vowel"
    else:
        return "Consonant"

char = input("Enter a character (a-z or A-Z): ")

if len(char) == 1 and char.isalpha():
    result = check_vowel_or_consonant(char)
    print(result)
else:
    print("Invalid input! Please enter a single alphabet character.")
