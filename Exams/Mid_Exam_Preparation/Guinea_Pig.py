food_kg = float(input())
hay_kg = float(input())
cover_kg = float(input())
weight_kg = float(input())

food_gr = food_kg * 1000
hay_gr = hay_kg * 1000
cover_gr = cover_kg * 1000
weight_gr = weight_kg * 1000

enough_food = True
for i in range(1, 31):
    food_gr -= 300
    if food_gr <= 0:
        print("Merry must go to the pet store!")
        enough_food = False
        break
    if i % 2 == 0:
        hay_gr -= 0.05 * food_gr
        if hay_gr <= 0:
            print("Merry must go to the pet store!")
            enough_food = False
            break

    if i % 3 == 0:
        cover_gr -= (1/3) * weight_gr
        if cover_gr <= 0:
            print("Merry must go to the pet store!")
            enough_food = False
            break

if enough_food:
    print(f"Everything is fine! Puppy is happy! Food: {(food_gr / 1000):.2f}, Hay: {(hay_gr / 1000):.2f}, Cover: {(cover_gr / 1000):.2f}.")