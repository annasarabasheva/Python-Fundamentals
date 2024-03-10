n = int(input())

for i in range(0, n):
    for j in range(0, n):
        for t in range(0, n):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + t)}")