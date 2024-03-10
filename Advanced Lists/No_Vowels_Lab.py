text = input()

vowels = ['a', 'o', 'u', 'e', 'i', "A", "O", "U", "E", "I"]

no_vowels = [el for el in text if el not in vowels]
print("".join(no_vowels))