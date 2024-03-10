import re

text = input()
pattern = r"\b(?P<day>\d{2})([\./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>[0-9]{4})\b"

dates = re.finditer(pattern, text)

for date in dates:
    print(f"Day: {date['day']}, Month: {date['month']}, Year: {date['year']}")