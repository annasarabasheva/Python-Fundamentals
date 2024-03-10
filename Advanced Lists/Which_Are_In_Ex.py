substrings = input().split(", ")
strings = input().split(", ")

new_list = []


for el in substrings:
    for j in strings:
        if el in j:
            if el not in new_list:
                new_list.append(el)



print(new_list)