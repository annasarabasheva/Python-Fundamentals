myList = input().split(", ")
myList.sort()
myList = sorted(myList, key=len, reverse=True)
print(myList)