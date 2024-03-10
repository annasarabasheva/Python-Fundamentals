import re

text = input()
pattern = r"(^|(?<=\s))([A-Za-z0-9]+[\.\-_]*[A-Za-z0-9]+@[a-zA-Z]+-*[a-zA-Z]+(\.[a-zA-Z]+-*[a-zA-Z]+)+)"

emails = re.findall(pattern, text)
for email in emails:
    print(email[1])
