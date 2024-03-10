message = input()
while True:
    line = input()
    if line == "Reveal":
        print(f"You have a new text message: {message}")
        break
    command_arg = line.split(":|:")
    command = command_arg[0]
    if command == "InsertSpace":
        index = int(command_arg[1])
        message = message[:index] + " " + message[index:]
        print(message)
    elif command == "Reverse":
        substring = command_arg[1]
        if substring in message:
           new_substring = substring[::-1]
           message = message.replace(substring, "", 1)
           message = message[:] + new_substring
           print(message)
        else:
            print("error")
    elif command == "ChangeAll":
        substring = command_arg[1]
        replacement = command_arg[2]
        message = message.replace(substring, replacement)
        print(message)
