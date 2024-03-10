words = []
while True:
    word = input()
    if word == "end":
        break
    words.append(word)

for word in words:
    new_word = word[::-1]
    print(f"{word} = {new_word}")
