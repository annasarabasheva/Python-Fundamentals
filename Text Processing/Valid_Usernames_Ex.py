special_characters = "!@#$%^&*()+?=,<>/ "
usernames = input().split(", ")
valid = []

for username in usernames:
    if 3 <= len(username) <= 16:
        if any(c in special_characters for c in username):
            continue
        else:
            valid.append(username)


for el in valid:
    print("".join(el))
