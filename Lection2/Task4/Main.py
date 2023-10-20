def is_vowel(char):
    vowels = "aeiouAEIOU"
    return char in vowels

something = input("Enter something: ")
vowels = [char for char in something if is_vowel(char)]

print("Vowels in a string:", " ".join(vowels))