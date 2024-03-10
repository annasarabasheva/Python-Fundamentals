status_pirate_ship = [int(el) for el in input().split(">") if int(el) in range(1, 1001)]
status_warship = [int(x) for x in input().split(">") if int(x) in range(1, 1001)]
max_health = int(input())

flag = True
while True:
    command_arg = input().split()
    command = command_arg[0]
    if command == "Retire":
        break

    if command == "Fire":
        index = int(command_arg[1])
        if -200 <= index <= 200:
            if index in range(len(status_warship)):
                before_reduction = status_warship[index]
                reduction = int(command_arg[2])
                if 1 <= reduction <= 1000:
                    after_reduction = before_reduction - reduction
                    if after_reduction <= 0:
                        print("You won! The enemy ship has sunken.")
                        flag = False
                        break
                    else:
                        status_warship.remove(before_reduction)
                        status_warship.insert(index, after_reduction)

            else:
                continue
        else:
            continue
    elif command == "Defend":
        start_index = int(command_arg[1])
        end_index = int(command_arg[2])
        if -200 <= start_index <= 200 and -200 <= end_index <= 200:
            reduction_pirate = int(command_arg[3])
            if 1 <= reduction_pirate <= 1000:
                if start_index in range(len(status_pirate_ship)) and end_index in range(len(status_pirate_ship)):
                    for i in range(start_index, end_index + 1):
                        before_pirate = status_pirate_ship[i]
                        after_pirate = before_pirate - reduction_pirate
                        if after_pirate <= 0:
                            print("You lost! The pirate ship has sunken.")
                            flag = False
                            break
                        else:
                            status_pirate_ship.remove(before_pirate)
                            status_pirate_ship.insert(i, after_pirate)
                else:
                    continue
            else:
                continue
        else:
            continue
    elif command == "Repair":
        index_p = int(command_arg[1])
        if -200 <= index_p <= 200:
            increase_with = int(command_arg[2])
            if 1 <= increase_with <= 1000:
                if index_p in range(len(status_pirate_ship)):
                    before_index_pirate = status_pirate_ship[index_p]
                    after_index_pirate = before_index_pirate + increase_with
                    status_pirate_ship.remove(before_index_pirate)
                    if after_index_pirate <= max_health:
                        status_pirate_ship.insert(index_p, after_index_pirate)
                    else:
                        status_pirate_ship.insert(index_p, max_health)

                else:
                    continue
            else:
                continue
        else:
            continue

    elif command == "Status":
        counter = 0
        for i in range(len(status_pirate_ship)):
            element = float(status_pirate_ship[i])
            percentages = float((element / float(max_health)))
            if percentages < 0.2:
                counter += 1

        print(f"{counter} sections need repair.")

if flag:
    print(f"Pirate ship status: {sum(status_pirate_ship)}\nWarship status: {sum(status_warship)}")





