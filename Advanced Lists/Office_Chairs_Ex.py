n_rooms = int(input())

free_chairs = 0
counter_room = 0
flag = True
for i in range(n_rooms):
    information = input().split()
    chairs = len(information[0])
    visitors = int(information[1])
    counter_room += 1
    if chairs > visitors:
        free_chairs += (chairs - visitors)

    if chairs < visitors:
        flag = False
        print(f"{visitors - chairs} more chairs needed in room {counter_room}")

if flag:
    print(f"Game On, {free_chairs} free chairs left")