word = input()
char = ""
for i in range(len(word) - 1, -1, -1):
    char += word[i]

print(char)