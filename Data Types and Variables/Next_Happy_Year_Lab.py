year = int(input())
year += 1
year_string = str(year)

while len(year_string) != len(set(year_string)):
    year += 1
    year_string = str(year)

print(year)