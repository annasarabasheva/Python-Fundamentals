n = int(input())
dic = {}
for i in range(n):
    line = input().split()
    hero = line[0]
    hp = min(int(line[1]), 100)
    mp = min(int(line[2]), 200)
    dic[hero] = [hp, mp]

while True:
    line = input()
    if line == "End":
        break
    command_arg = line.split(" - ")
    command = command_arg[0]
    hero_name = command_arg[1]
    if command == "CastSpell":
        mp_needed = int(command_arg[2])
        spell_name = command_arg[3]
        if dic[hero_name][1] >= mp_needed:
            dic[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {dic[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command == "TakeDamage":
        damage = int(command_arg[2])
        attacker = command_arg[3]
        dic[hero_name][0] -= damage
        if dic[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {dic[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del dic[hero_name]
    elif command == "Recharge":
        amount = int(command_arg[2])
        old_mp = dic[hero_name][1]
        dic[hero_name][1] += amount
        if dic[hero_name][1] > 200:
            dic[hero_name][1] = 200
            print(f"{hero_name} recharged for {200 - old_mp} MP!")
        else:
            print(f"{hero_name} recharged for {amount} MP!")
    elif command == "Heal":
        amount = int(command_arg[2])
        old_hp = dic[hero_name][0]
        dic[hero_name][0] += amount
        if dic[hero_name][0] > 100:
            dic[hero_name][0] = 100
            print(f"{hero_name} healed for {100 - old_hp} HP!")
        else:
            print(f"{hero_name} healed for {amount} HP!")

for hero in dic:
    print(hero)
    print(f"  HP: {dic[hero][0]}")
    print(f"  MP: {dic[hero][1]}")