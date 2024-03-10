n = int(input())
dic = {}
for i in range(n):
    name = input()
    grade = float(input())
    if name not in dic:
        dic[name] = [grade]
    else:
        dic[name].append(grade)


for key, value in dic.items():
    dic[key] = sum(value) / len(value)


for key, value in dic.items():
    if value >= 4.50:
        print(f"{key} -> {value:.2f}")
