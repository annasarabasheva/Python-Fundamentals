import re
list = []
total_cost = 0
while True:
    line = input()
    if line == "Purchase":
        break
    pattern = r"^>>([a-zA-Z]+)<<(\d+(\.\d+)?)!(\d+)$"
    results = re.findall(pattern, line)
    if not results:
        continue
    groups = results[0]
    furniture = groups[0]
    price = float(groups[1])
    quantity = int(groups[3])
    cost = price * quantity
    total_cost += cost
    list.append(furniture)


print("Bought furniture:")
for el in list:
    print(el)

print(f"Total money spend: {total_cost:.2f}")