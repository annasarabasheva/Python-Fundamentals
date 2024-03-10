n = int(input())
dic = {}
for i in range(n):
    word = input()
    synonym = input()
    if word in dic:
        dic[word].append(synonym)
        continue
    dic[word] = [synonym]


for key, value in dic.items():
    print(f"{key} - {', '.join(value)}")