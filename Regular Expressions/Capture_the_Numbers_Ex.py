import re
list = []
while True:
    line = input()
    if line == "":
        break

    pattern = r"\d+"
    numbers = re.findall(pattern, line)
    if len(numbers) > 0:
        list.append(numbers)


for l in list:
    print(*l, end=" ")