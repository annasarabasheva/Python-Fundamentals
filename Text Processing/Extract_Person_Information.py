import re

n = int(input())
name_pattern = r"@([a-zA-Z]+)\|"
age_pattern = r"#(\d+)\*"
for i in range(n):
    line = input()
    name = re.findall(name_pattern, line)
    age = re.findall(age_pattern, line)
    print(f"{''.join(name)} is {''.join(age)} years old.")
