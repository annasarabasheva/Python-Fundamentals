dic = {}
while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource in dic:
        dic[resource] += quantity
        continue
    dic[resource] = quantity


for key, value in dic.items():
    print(f"{key} -> {value}")