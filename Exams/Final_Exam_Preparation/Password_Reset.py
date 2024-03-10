text = input()
while True:
    line = input()
    if line == "Done":
        print(f"Your password is: {text}")
        break
    command_arg = line.split()
    command = command_arg[0]
    if command == "TakeOdd":
        new_word = ""
        for i in range(len(text)):
            if i % 2 != 0:
                letter = text[i]
                new_word += letter
        text = new_word
        print(text)
    elif command == "Cut":
        index = int(command_arg[1])
        length = int(command_arg[2])
        substring = text[index:index + length]
        text = text.replace(substring, "", 1)
        print(text)
    elif command == "Substitute":
        substring = command_arg[1]
        substitute = command_arg[2]
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")