dic = {}
while True:
    line = input()
    if line == "End":
        break
    args = line.split(" -> ")
    name = args[0]
    id = args[1]
    if name not in dic:
        dic[name] = [id]

    else:
        if id not in dic[name]:
            dic[name].append(id)


for key, value in dic.items():
    print(key)
    for val in value:
        print(f"-- {val}")