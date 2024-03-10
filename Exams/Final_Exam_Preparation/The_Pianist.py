n = int(input())
dic = {}
for i in range(n):
    line = input().split("|")
    piece = line[0]
    composer = line[1]
    key = line[2]
    dic[piece] = [composer, key]

while True:
    line = input()
    if line == "Stop":
        break
    command_arg = line.split("|")
    command = command_arg[0]
    piece = command_arg[1]
    if command == "Add":
        composer = command_arg[2]
        key = command_arg[3]
        if piece in dic:
            print(f"{piece} is already in the collection!")
            continue
        else:
            dic[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command == "Remove":
        if piece in dic:
            print(f"Successfully removed {piece}!")
            del dic[piece]
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command == "ChangeKey":
        new_key = command_arg[2]
        if piece in dic:
            dic[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")


for p in dic:
    print(f"{p} -> Composer: {dic[p][0]}, Key: {dic[p][1]}")