groceries_list = input().split("!")

while True:
    command_arg = input().split()
    if command_arg == ["Go", "Shopping!"]:
        print(", ".join(groceries_list))
        break
    else:
        command = command_arg[0]

        if command == "Urgent":
            urgent_item = command_arg[1]
            if urgent_item not in groceries_list:
                groceries_list.insert(0, urgent_item)

            else:
                continue

        elif command == "Unnecessary":
            unnecessary_item = command_arg[1]
            if unnecessary_item not in groceries_list:
                continue
            else:
                groceries_list.remove(unnecessary_item)

        elif command == "Correct":
            old_item = command_arg[1]
            new_item = command_arg[2]
            if old_item not in groceries_list:
                continue
            else:
                groceries_list = list(map(lambda x: x.replace(old_item, new_item), groceries_list))

        elif command == "Rearrange":
            rearranged_item = command_arg[1]
            if rearranged_item not in groceries_list:
                continue
            else:
                groceries_list.remove(rearranged_item)
                groceries_list.append(rearranged_item)



