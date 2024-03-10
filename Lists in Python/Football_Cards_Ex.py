card = input().split()

team_a = 11
team_b = 11
players_sent_home = []
for el in card:
    card_args = el.split("-")
    team = card_args[0]
    number = card_args[1]
    if el in players_sent_home:
        continue
    if team == "A":
        team_a -= 1
        players_sent_home.append(el)
    elif team == "B":
        team_b -= 1
        players_sent_home.append(el)

    if team_a < 7 or team_b < 7:
        print(f"Team A - {team_a}; Team B - {team_b}")
        print("Game was terminated")
        exit()

print(f"Team A - {team_a}; Team B - {team_b}")
