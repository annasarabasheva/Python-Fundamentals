electrons = int(input())

list_shells = []
while electrons > 0:
    n = len(list_shells) + 1
    shell_value = min(2 * (n**2), electrons)
    list_shells.append(shell_value)
    electrons -= shell_value



print(list_shells)