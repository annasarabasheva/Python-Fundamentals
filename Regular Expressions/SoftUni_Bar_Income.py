import re
pattern = r"%([A-Z][a-z]+)%\w*<(\w+)>\w*\|(\d+)\|[a-zA-Z]*(\d+|[0-9]+\.[0-9]+)\$"
list_date = []
while True:
    line = input()
    if line == "end of shift":
        break
    date = re.findall(pattern, line)
    if len(date) == 0:
        continue
    list_date.append(date)


total_income = 0
for i in range(len(list_date)):
    total_income += int(list_date[i][0][2])*float(list_date[i][0][3])
    print(f"{list_date[i][0][0]}: {list_date[i][0][1]} - {(int(list_date[i][0][2])*float(list_date[i][0][3])):.2f}")

print(f"Total income: {total_income:.2f}")