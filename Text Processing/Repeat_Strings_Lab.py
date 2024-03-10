words = input().split()
result = ""
for word in words:
    new_word = word * len(word)
    result += new_word


print(result)