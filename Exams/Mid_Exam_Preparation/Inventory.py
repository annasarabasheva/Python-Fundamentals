items = input().split(", ")

while True:
    line = input()
    if line == "Craft!":
        print(", ".join(items))
        break
    command_item = line.split(" - ")
    command = command_item[0]
    item = command_item[1]
    if command == "Collect":
        if item not in items:
            items.append(item)
    elif command == "Drop":
        if item in items:
            items.remove(item)
    elif command == "Combine Items":
        item_split = item.split(":")
        old_item = item_split[0]
        new_item = item_split[1]
        if old_item in items:
            idx_old = items.index(old_item)
            idx_new = idx_old + 1
            items.insert(idx_new, new_item)
    elif command == "Renew":
        if item in items:
            items.remove(item)
            items.append(item)



