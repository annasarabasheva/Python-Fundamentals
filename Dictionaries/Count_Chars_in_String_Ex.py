line = input()
dic = {}
for el in line:
    if el == " ":
        continue
    if el not in dic:
        dic[el] = 1
    elif el in dic:
        dic[el] += 1

for key, value in dic.items():
    print(f"{key} -> {value}")


