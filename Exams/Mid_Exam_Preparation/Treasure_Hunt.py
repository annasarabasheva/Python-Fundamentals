treasures = input().split("|")

while True:
    line = input()
    if line == "Yohoho!":
        if len(treasures) > 0:
            sum_length = 0
            for i in range(len(treasures)):
                el = treasures[i]
                length = len(el)
                sum_length += length
            average_gain = sum_length / len(treasures)
            print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
        else:
            print("Failed treasure hunt.")
        break
    command_arg = line.split()
    command = command_arg[0]
    if command == "Loot":
        for i in range(1, len(command_arg)):
            element = command_arg[i]
            if element in treasures:
                continue
            else:
                treasures.insert(0, element)
    elif command == "Drop":
        idx = int(command_arg[1])
        if idx in range(len(treasures)):
            treasure = treasures[idx]
            treasures.remove(treasure)
            treasures.append(treasure)
    elif command == "Steal":
        count = int(command_arg[1])
        if count < len(treasures):
            first_idx = len(treasures) - count
            stolen_treasures = treasures[-count:]
            print(", ".join(stolen_treasures))
            del treasures[first_idx:]
        elif count >= len(treasures):
            removed_items =[]
            for i in range(len(treasures)):
                ele = treasures[i]
                removed_items.append(ele)
            print(", ".join(removed_items))
            treasures.clear()






