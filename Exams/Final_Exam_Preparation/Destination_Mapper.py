import re

text = input()
pattern = r"(=|/)([A-Z][a-zA-Z]{2,})\1"

locations = re.findall(pattern, text)
sum_len = 0
list_dest = []
for loc in locations:
    destination = loc[1]
    list_dest.append(destination)
    sum_len += len(destination)

print(f"Destinations: {', '.join(list_dest)}\nTravel Points: {sum_len}")