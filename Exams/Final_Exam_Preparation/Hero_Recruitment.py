dic_heroes = {}
while True:
    line = input()
    if line == "End":
        break
    command_arg = line.split()
    command = command_arg[0]
    hero_name = command_arg[1]
    if command == "Enroll":
        if hero_name not in dic_heroes:
            dic_heroes[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")
    elif command == "Learn":
        spell_name = command_arg[2]
        if hero_name not in dic_heroes:
            print(f"{hero_name} doesn't exist.")
        elif hero_name in dic_heroes:
            if spell_name not in dic_heroes[hero_name]:
                dic_heroes[hero_name].append(spell_name)
            else:
                print(f"{hero_name} has already learnt {spell_name}.")
    elif command == "Unlearn":
        spell_name = command_arg[2]
        if hero_name not in dic_heroes:
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in dic_heroes[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        elif spell_name in dic_heroes[hero_name]:
            dic_heroes[hero_name].remove(spell_name)


print("Heroes:")
for key in dic_heroes:
    print(f"== {key}: {', '.join(dic_heroes[key])}")