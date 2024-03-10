rooms = input().split("|")
initial_health = 100
initial_bitcoins = 0
max_health = 100
counter_rooms = 0

flag = True
for room in rooms:
    command_arg = room.split()
    command = command_arg[0]
    number = int(command_arg[1])
    counter_rooms += 1
    if command == "potion":
        if initial_health < max_health:
            current_initial_health = initial_health
            initial_health = min((number + initial_health), max_health)
            amount = initial_health - current_initial_health
            print(f"You healed for {amount} hp.")
            print(f"Current health: {initial_health} hp.")
        else:
            initial_health = max_health
            print(f"You healed for 0 hp.")
            print(f"Current health: {max_health} hp.")

    elif command == "chest":
        initial_bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        initial_health -= number
        if initial_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {counter_rooms}")
            flag = False
            break

if flag:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")
