text = input()
while True:
    line = input()
    if line == "Done":
        break
    command_arg = line.split()
    command = command_arg[0]
    if command == "Change":
        char = command_arg[1]
        replacement = command_arg[2]
        text = text.replace(char, replacement)
        print(text)
    elif command == "Includes":
        substring = command_arg[1]
        if substring in text:
            print("True")
        else:
            print("False")
    elif command == "End":
        substring = command_arg[1]
        if text.endswith(substring):
            print("True")
        else:
            print("False")
    elif command == "Uppercase":
        text = text.upper()
        print(text)
    elif command == "FindIndex":
        char = command_arg[1]
        index = text.find(char)
        print(index)
    elif command == "Cut":
        start_idx = int(command_arg[1])
        count = int(command_arg[2])
        cut_part = text[start_idx:start_idx + count]
        print(cut_part)
