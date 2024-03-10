import re
line = input().lower()
word = input().lower()
pattern = fr"\b({word})\b"
print(len(re.findall(pattern, line)))