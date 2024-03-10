number = int(input())

def percentages(n):

    list_percents = ""

    for i in range(0, n, 10):
        if i % 10 == 0:
            list_percents += "%"

    for j in range(n, 100, 10):
        if j % 10 == 0:
            list_percents += "."

    no_strings = list_percents.lstrip(" \' ")

    if n < 100:
        print(f"{n}% [{no_strings}]")
        print("Still loading...")


    if n == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")


percentages(number)