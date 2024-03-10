needed_experience = float(input())
count_battles = int(input())
initial_experience = 0
counter = 0
if needed_experience > 0 and count_battles > 0:
    for battle in range(1, count_battles + 1):
        earned_experience = float(input())
        initial_experience += earned_experience
        counter += 1
        if battle % 15 ==0:
            initial_experience += earned_experience * 0.05
        if battle % 3 == 0:
            initial_experience += earned_experience * 0.15
        if battle % 5 == 0:
            initial_experience -= earned_experience * 0.1

        if initial_experience >= needed_experience:
            break


    if initial_experience < needed_experience:
        print(f"Player was not able to collect the needed experience, {(needed_experience - initial_experience):.2f} more needed.")
    elif initial_experience >= needed_experience:
        print(f"Player successfully collected his needed experience for {counter} battles.")

