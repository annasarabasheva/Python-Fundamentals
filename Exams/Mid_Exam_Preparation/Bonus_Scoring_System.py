from math import ceil
n_students = int(input())
n_lectures = int(input())
additional_bonus = int(input())

all_bonuses = []
lectures_att = []
if 0 <= n_students <= 50 and 0 <= n_lectures <= 50 and 0 <= additional_bonus <= 100:

    for i in range(n_students):
        attendance = int(input())
        if attendance not in lectures_att:
            lectures_att.append(attendance)

        bonus = ceil((attendance / n_lectures) * (5 + additional_bonus))
        all_bonuses.append(bonus)
    if len(lectures_att) > 0 and len(all_bonuses) > 0:

        max_lecture = max(lectures_att)
        max_bonus = max(all_bonuses)

        print(f"Max Bonus: {max_bonus}.")
        print(f"The student has attended {max_lecture} lectures.")
    else:
        print(f"Max Bonus: 0.")
        print(f"The student has attended 0 lectures.")

