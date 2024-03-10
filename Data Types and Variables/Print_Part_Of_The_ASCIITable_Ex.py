first = int(input())
second = int(input())

sum_elements = ""
for i in range(first, second + 1):
    sum_elements += chr(i) + " "

print(sum_elements)