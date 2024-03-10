while True:
    name = input()
    if name == "End":
        break
    if name == "SoftUni":
        continue
    j = len(name)
    i = 0
    res = []
    while i < j:
        res.append(name[i] * 2)
        i = i + 1
    result = "".join(res)
    print(result)