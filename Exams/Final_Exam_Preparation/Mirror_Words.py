import re
text = input()
pattern = r"(@|#)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"
pairs = re.findall(pattern, text)
mirrored_words = []
for i in range(len(pairs)):
    first_word = pairs[i][1]
    second_word = pairs[i][2]
    if first_word == second_word[::-1]:
        mirrored_words.append(first_word)
        mirrored_words.append(second_word)

if len(pairs) == 0:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f"{len(pairs)} word pairs found!")
    if len(mirrored_words) == 0:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        list = []
        for i in range(len(pairs)):
            first_word = pairs[i][1]
            second_word = pairs[i][2]
            if first_word == second_word[::-1]:
                list.append(f"{first_word} <=> {second_word}")
        print(', '.join(list))



