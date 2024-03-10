n = int(input())
dic = {}
for i in range(n):
    text = input().split("|")
    car_a = text[0]
    mileage_a = int(text[1])
    fuel_a = int(text[2])
    dic[car_a] = [mileage_a, fuel_a]

while True:
    line = input()
    if line == "Stop":
        break
    command_arg = line.split(" : ")
    command = command_arg[0]
    if command == "Drive":
        car = command_arg[1]
        distance = int(command_arg[2])
        fuel = int(command_arg[3])
        if dic[car][1] < fuel:
            print("Not enough fuel to make that ride")
            continue
        dic[car][1] -= fuel
        dic[car][0] += distance
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if dic[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            del dic[car]
    elif command == "Refuel":
        car = command_arg[1]
        old_fuel = dic[car][1]
        fuel = int(command_arg[2])
        dic[car][1] = min(dic[car][1] + fuel, 75)
        print(f"{car} refueled with {dic[car][1] - old_fuel} liters")
    elif command == "Revert":
        car = command_arg[1]
        kilometers = int(command_arg[2])
        dic[car][0] -= kilometers
        if dic[car][0] < 10000:
            dic[car][0] = 10000
            continue
        print(f"{car} mileage decreased by {kilometers} kilometers")

for car in dic:
    print(f"{car} -> Mileage: {dic[car][0]} kms, Fuel in the tank: {dic[car][1]} lt.")