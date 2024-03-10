lost_games = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
sum_expenses = 0

for i in range(1, lost_games + 1):
    if i % 2 == 0:
        sum_expenses += helmet_price
    if i % 3 == 0:
        sum_expenses += sword_price
    if i % 6 == 0:
        sum_expenses += shield_price
    if i % 12 == 0:
        sum_expenses += armor_price

print(f"Gladiator expenses: {sum_expenses:.2f} aureus")