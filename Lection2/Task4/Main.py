def is_vowel(char):
    vowels = "aeiouAEIOU"
    return char in vowels

something = input("Enter something: ")
vowels_set = set(char for char in something if is_vowel(char))
vowels = sorted(list(vowels_set))

print("Unique vowels in a string:", " ".join(vowels))
