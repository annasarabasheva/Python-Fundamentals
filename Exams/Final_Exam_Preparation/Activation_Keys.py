activation_key = input()
while True:
    line = input()
    if line == "Generate":
        print(f"Your activation key is: {activation_key}")
        break

    command_arg = line.split(">>>")
    command = command_arg[0]
    if command == "Contains":
        substring = command_arg[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command == "Flip":
        state = command_arg[1]
        start = int(command_arg[2])
        end = int(command_arg[3])
        if state == "Upper":
            activation_key = activation_key[:start] + activation_key[start:end].upper() +  activation_key[end:]
            print(activation_key)
        elif state == "Lower":
            activation_key = activation_key[:start] + activation_key[start:end].lower() + activation_key[end:]
            print(activation_key)
    elif command == "Slice":
        start_idx = int(command_arg[1])
        end_idx = int(command_arg[2])
        activation_key = activation_key[:start_idx] + activation_key[end_idx:]
        print(activation_key)