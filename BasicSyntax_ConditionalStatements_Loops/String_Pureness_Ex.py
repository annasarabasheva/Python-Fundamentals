import re

n = int(input())

for i in range(n):
    string = input()
    regex = re.compile('[_,.]')
    if (regex.search(string) == None):
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
