import re
n = int(input())
pattern = r"\|([A-Z]{4,})\|:#([A-Za-z]+\s[A-Za-z]+)#"
for i in range(n):
    line = input()
    boss_title = re.findall(pattern, line)
    if len(boss_title) == 0:
        print("Access denied!")
    else:
        boss_name = boss_title[0][0]
        title = boss_title[0][1]
        print(f"{boss_name}, The {title}\n>> Strength: {len(boss_name)}\n>> Armor: {len(title)}")