dic = {}
while True:
    line = input()
    if line == "end of contests":
        break
    command_arg = line.split(":")
    contest = command_arg[0]
    password = command_arg[1]
    dic[contest] = {}
    dic[contest]["password"] = password
while True:
    line = input()
    if line == "end of submissions":
        break
    command_arg = line.split("=>")
    contest = command_arg[0]
    password = command_arg[1]
    username = command_arg[2]
    points = int(command_arg[3])
    if contest in dic:
        if dic[contest]["password"] == password:
            if username not in dic[contest]:
                dic[contest]["username"] = [username]
                dic[contest]["points"] = points
            elif username in dic[contest]["username"]:
                dic[contest]["username"].append(username)


                if points > dic[contest]["points"]:
                    dic[contest]["points"] = points
                else:
                    continue


print(dic)