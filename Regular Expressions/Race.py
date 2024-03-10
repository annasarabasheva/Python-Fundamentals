import re
from collections import Counter
participants = input().split(", ")
pattern_name = r"[a-zA-Z]"
pattern_distance = r"\d"
dic = {}
while True:
    line = input()
    if line == "end of race":
        break
    letters = re.findall(pattern_name, line)
    name = ''.join(letters)
    if name in participants:
        digits = re.findall(pattern_distance, line)
        distance = 0
        for i in range(len(digits)):
            number = int(digits[i])
            distance += number
        if name in dic:
            dic[name] += distance
        else:
            dic[name] = distance

k = Counter(dic)
high = k.most_common(3)
for i in range(len(high)):
    if i == 0:
        print(f"1st place: {high[0][0]}")
    elif i == 1:
        print(f"2nd place: {high[1][0]}")
    elif i == 2:
        print(f"3rd place: {high[2][0]}")
