text = input().split()
palindrom = input()
result = list(filter(lambda x: (x == "".join(reversed(x))), text))
print(result)

counter_palindrom = 0

for el in result:
    if el == palindrom:
        counter_palindrom += 1

print(f"Found palindrome {counter_palindrom} times")