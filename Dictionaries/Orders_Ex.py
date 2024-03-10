dic = {}
while True:
    line = input()
    if line == "buy":
        break
    command_line = line.split()
    name = command_line[0]
    price = float(command_line[1])
    quantity = float(command_line[2])
    if name not in dic:
        dic[name] = [price, quantity]
    else:
        dic[name][0] = price
        dic[name][1] += quantity


for key, value in dic.items():
    print(f"{key} -> {(dic[key][0] * dic[key][1]):.2f}")