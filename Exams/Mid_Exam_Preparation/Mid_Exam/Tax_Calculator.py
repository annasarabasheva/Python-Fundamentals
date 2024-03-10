vehicles = input().split(">>")
total_tax = 0
for i in range(len(vehicles)):
    element = vehicles[i]
    car_years_kilometers = element.split()
    car_type = car_years_kilometers[0]
    if car_type not in ["family", "heavyDuty", "sports"]:
        print("Invalid car type.")
        continue
    years = int(car_years_kilometers[1])
    kilometers = int(car_years_kilometers[2])
    if car_type == "family":
        tax = int((kilometers / 3000)) * 12 + (50 - years * 5)
        total_tax += tax
        print(f"A {car_type} car will pay {tax:.2f} euros in taxes.")
    elif car_type == "heavyDuty":
        tax = int((kilometers / 9000)) * 14 + (80 - years * 8)
        total_tax += tax
        print(f"A {car_type} car will pay {tax:.2f} euros in taxes.")
    elif car_type == "sports":
        tax = int((kilometers / 2000)) * 18 + (100 - years * 9)
        total_tax += tax
        print(f"A {car_type} car will pay {tax:.2f} euros in taxes.")


print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")