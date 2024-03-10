text = input()
emoticons = []
for i in range(len(text)):
    el = text[i]
    if el == ":":
        emoticons.append(el + text[i + 1])

for em in emoticons:
    print(''.join(em))