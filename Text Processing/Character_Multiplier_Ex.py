text = input().split()
first = text[0]
second = text[1]
min_len = min(len(first), len(second))
result = 0

for i in range(min_len):
    first_char = first[i]
    second_char = second[i]
    result += ord(first_char) * ord(second_char)


for i in range(min_len, len(first)):
    char = first[i]
    result += ord(char)

for i in range(min_len, len(second)):
    char = second[i]
    result += ord(char)

print(result)


