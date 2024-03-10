import re
matches = []
while True:
    line = input()
    if line == "":
        break

    pattern = r"\b(www\.[a-zA-Z0-9\-]+(\.[a-z]+)+)\b"
    match = re.findall(pattern, line)
    if not match:
        continue
    group = match[0]
    email = group[0]
    matches.append(email)

for mail in matches:
    print(mail)