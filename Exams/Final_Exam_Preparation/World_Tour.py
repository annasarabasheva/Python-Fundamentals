countries = input()
while True:
    line = input()
    if line == "Travel":
        print(f"Ready for world tour! Planned stops: {countries}")
        break
    command_arg = line.split(":")
    command = command_arg[0]
    if command == "Add Stop":
        index = int(command_arg[1])
        string = command_arg[2]
        if index in range(len(countries)):
            countries = countries[:index] + string + countries[index:]
            print(countries)
        else:
            print(countries)
    elif command == "Remove Stop":
        start_idx = int(command_arg[1])
        end_idx = int(command_arg[2])
        if start_idx in range(len(countries)) and end_idx in range(len(countries)):
            countries = countries[:start_idx] + countries[end_idx + 1:]
            print(countries)
        else:
            print(countries)
    elif command == "Switch":
        old = command_arg[1]
        new = command_arg[2]
        if old in countries:
            countries = countries.replace(old, new)
            print(countries)
        else:
            print(countries)

