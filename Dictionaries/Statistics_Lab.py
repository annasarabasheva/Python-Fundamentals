dic = {}

while True:
    line = input()
    if line == "statistics":
        break

    command_line = line.split(": ")
    product = command_line[0]
    quantity = int(command_line[1])
    if product in dic:
        dic[product] += quantity
        continue
    dic[product] = quantity


print("Products in stock:")
sum_quantity = 0
for el in dic:
    print(f"- {el}: {dic[el]}")
    sum_quantity += dic[el]
print(f"Total Products: {len(dic)}\nTotal Quantity: {sum_quantity}")