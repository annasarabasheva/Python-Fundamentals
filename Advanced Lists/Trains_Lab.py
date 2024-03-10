number_wagons = int(input())
list_wag = [0] * number_wagons
new_list = list_wag

while True:
    command_arg = input().split(" ")
    command = command_arg[0]
    if command == "End":
        print(new_list)
        break
    arg = int(command_arg[1])

    if command == "add":
        new_list[-1] = new_list[-1] + arg

    elif command == "insert":
        new_list[arg] = new_list[arg] + int(command_arg[2])

    elif command == "leave":
        new_list[arg] = new_list[arg] - int(command_arg[2])








