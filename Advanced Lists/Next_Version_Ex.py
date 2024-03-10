version = [int(el) for el in input().split(".")]
first = version[0]
second = version[1]
third = version[2]

if third < 9:
    third += 1

elif third == 9:
    third = 0
    if second < 9:
        second += 1
    elif second == 9:
        second = 0
        first += 1


print(f"{first}.{second}.{third}")