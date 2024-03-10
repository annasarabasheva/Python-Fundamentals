n = int(input())
dic = {}
for i in range(n):
    line = input().split()
    status = line[0]
    username = line[1]
    if status == "unregister":
        if username not in dic:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            dic.pop(username)
        continue
    number = line[2]
    if status == "register":
        if username not in dic:
            dic[username] = number
            print(f"{username} registered {number} successfully")
        else:
            print(f"ERROR: already registered with plate number {number}")

for key, value in dic.items():
    print(f"{key} => {value}")
