n = int(input())
sum_n = 0
for i in range(n):
    letter = input()
    sum_n += ord(letter)

print(f"The sum equals: {sum_n}")