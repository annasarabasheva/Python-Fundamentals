n = int(input())
dic = {}
for i in range(n):
    line = input().split("<->")
    plant = line[0]
    rarity = int(line[1])
    dic[plant] = {}
    dic[plant]["rarity"] = rarity
while True:
    line = input()
    if line == "Exhibition":
        break
    command_arg = line.split(": ")
    command = command_arg[0]
    rest = command_arg[1]
    another_split = rest.split(" - ")
    plant = another_split[0]
    if command == "Rate":
        rating = int(another_split[1])
        if plant in dic and "rating" in dic[plant]:
            dic[plant]["rating"].append(rating)
        elif plant in dic and "rating" not in dic[plant]:
            dic[plant]["rating"] = [rating]
        elif plant not in dic:
            print("error")
    elif command == "Update":
        new_rarity = int(another_split[1])
        if plant in dic:
            dic[plant]["rarity"] = new_rarity
        else:
            print("error")
    elif command == "Reset":
        if plant in dic:
            del dic[plant]["rating"]
        else:
            print("error")
print("Plants for the exhibition:")
for p in dic:
    if "rating" not in dic[p]:
        print(f"- {p}; Rarity: {dic[p]['rarity']}; Rating: 0.00")
    else:
        average = sum(dic[p]['rating'])/len(dic[p]['rating'])
        print(f"- {p}; Rarity: {dic[p]['rarity']}; Rating: {average:.2f}")