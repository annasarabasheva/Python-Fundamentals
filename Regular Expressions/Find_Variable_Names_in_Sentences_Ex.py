import re

line = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
valid_names = re.findall(pattern, line)
print(",".join(valid_names))