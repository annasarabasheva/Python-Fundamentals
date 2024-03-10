import re
from math import floor
text = input()
pattern = r"(#|\|)([a-zA-Z\s]+)\1([0-9]{2}/[0-9]{2}/[0-9]{2})\1(\b(10000|[0-9][0-9]{0,3})\b)\1"
food = re.findall(pattern, text)
if len(food) > 0:
    sum_calories = 0
    for i in range(len(food)):
        calories = int(food[i][3])
        sum_calories += calories

    days = floor(sum_calories / 2000)
    if days > 0:
        print(f"You have food to last you for: {days} days!")
        for idx in range(len(food)):
            f = food[idx][1]
            date = food[idx][2]
            cal = food[idx][3]
            print(f"Item: {f}, Best before: {date}, Nutrition: {cal}")
    else:
        print("You have food to last you for: 0 days!")
        for idx in range(len(food)):
            f = food[idx][1]
            date = food[idx][2]
            cal = food[idx][3]
            print(f"Item: {f}, Best before: {date}, Nutrition: {cal}")

else:
    print("You have food to last you for: 0 days!")
