
from math import ceil
first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())

sum_employees = first_employee + second_employee + third_employee
hours_passed = 0
if students_count > 0:
    while students_count > 0 or hours_passed % 4 == 0:
        if hours_passed % 4 == 0 and hours_passed != 0:
            hours_passed += 1
            continue

        students_count -= sum_employees
        hours_passed += 1

print(f"Time needed: {hours_passed}h.")
