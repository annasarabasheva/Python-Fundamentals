days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

total_plunder = 0
if days > 0:
    for i in range(1, days + 1):
        total_plunder += daily_plunder
        if i % 3 == 0:
            total_plunder += (daily_plunder * 0.5)

        if i % 5 == 0:
            total_plunder -= 0.3 * total_plunder

    if total_plunder >= expected_plunder:
        print(f"Ahoy! {total_plunder:.2f} plunder gained.")
    else:
        percentage = (total_plunder / expected_plunder) * 100
        print(f"Collected only {percentage:.2f}% of the plunder.")
else:
    print(f"Collected 0% of the plunder.")
