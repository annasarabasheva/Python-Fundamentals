line = input().lower().split()

dic = {}
for el in line:
    if el not in dic:
        dic[el] = 1
    elif el in dic:
        dic[el] += 1


for key, value in dic.items():
    if value % 2 != 0:
        print(key, end=" ")

