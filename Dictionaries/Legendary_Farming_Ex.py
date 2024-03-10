dic = {}
line = input()
while line != "":
    new_line = line.split()
    for i in range(0, len(new_line), 2):
        value = int(new_line[i])
        key = new_line[i + 1].lower()
        if key in dic:
            dic[key] += value
            if key == "shards":
                if dic[key] >= 250:
                    break
            elif key == "fragments":
                if dic[key] >= 250:
                    break
            elif key == "motes":
                if dic[key] >= 250:
                    break
        else:
            dic[key] = value
            if key == "shards":
                if dic[key] >= 250:
                    break
            elif key == "fragments":
                if dic[key] >= 250:
                    break
            elif key == "motes":
                if dic[key] >= 250:
                    break
    for key, value in dic.items():
        if key == "shards":
            if dic[key] >= 250:
                print("Shadowmourne obtained!")
                dic[key] -= 250
                print(
                    f"shards: {dic.get('shards', 0)}\nfragments: {dic.get('fragments', 0)}\nmotes: {dic.get('motes', 0)}")

                for key, value in dic.items():
                    if key not in ["shards", "fragments", "motes"]:
                        print(f"{key}: {value}")

                exit()
        elif key == "fragments":
            if dic[key] >= 250:
                print("Valanyr obtained!")
                dic[key] -= 250
                print(
                    f"shards: {dic.get('shards', 0)}\nfragments: {dic.get('fragments', 0)}\nmotes: {dic.get('motes', 0)}")

                for key, value in dic.items():
                    if key not in ["shards", "fragments", "motes"]:
                        print(f"{key}: {value}")

                exit()
        elif key == "motes":
            if dic[key] >= 250:
                print("Dragonwrath obtained!")
                dic[key] -= 250
                print(
                    f"shards: {dic.get('shards', 0)}\nfragments: {dic.get('fragments', 0)}\nmotes: {dic.get('motes', 0)}")

                for key, value in dic.items():
                    if key not in ["shards", "fragments", "motes"]:
                        print(f"{key}: {value}")


                exit()
    line = input()




