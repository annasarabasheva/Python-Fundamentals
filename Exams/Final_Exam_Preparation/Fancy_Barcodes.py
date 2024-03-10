import re
n = int(input())
pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

for i in range(n):
    barcode = input()
    its_valid = re.findall(pattern, barcode)
    if its_valid:
        bar = its_valid[0]
        list_digit = []
        for el in bar:
            if el.isdigit():
                list_digit.append(el)
        if len(list_digit) == 0:
            print("Product group: 00")
        else:
            print(f"Product group: {''.join(list_digit)}")

    else:
        print("Invalid barcode")

