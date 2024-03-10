n = int(input())
for i in range(1, n + 1):
    i_string = str(i)
    sum_strings = 0
    for char in i_string:
        sum_strings += int(char)
    if sum_strings == 5 or sum_strings == 7 or sum_strings == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
