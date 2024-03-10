text = input()
new_text = []
for el in text:
    new_el = chr(ord(el) + 3)
    new_text.append(new_el)

print(''.join(new_text))