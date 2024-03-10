countries = input().split(", ")
capitals = input().split(", ")

dic = {}
result = zip(countries, capitals)

for el in result:
    element = list(el)
    key = element[0]
    value = element[1]
    dic[key] = value

for key, value in dic.items():
    print(f"{key} -> {value}")
