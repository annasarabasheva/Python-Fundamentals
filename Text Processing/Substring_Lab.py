unwanted = input()
wanted = input()

while unwanted in wanted:
    wanted = wanted.replace(unwanted, "")


print(wanted)
