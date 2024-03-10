import re
text = input()
pattern_emojis = r"(::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*)"
pattern_numbers = r"\d"
emojis = re.findall(pattern_emojis, text)
numbers = re.findall(pattern_numbers, text)
list_em = []
for e in range(len(emojis)):
    list_em.append(emojis[e])

max_coolness = 1
for n in numbers:
    max_coolness *= int(n)

res = []
for element in list_em:
    ascii_sum = 0
    for ch in element:
        if ch.isalpha():
            ascii_sum += ord(ch)
    if ascii_sum > max_coolness:
        res.append(element)

print(f"Cool threshold: {max_coolness}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for el in res:
    print(el)