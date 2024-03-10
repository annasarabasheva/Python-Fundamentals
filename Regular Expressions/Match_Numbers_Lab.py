import re

text = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

numbers = re.finditer(pattern, text)

for number in numbers:
    n = number.group()
    print(n, end=' ')



