from math import ceil


def every_4th_element(items, n):
  results = []
  for i, value in enumerate(items):
    if i % n == 0 and i != 0:
      results.append(value)
  return results


first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())

students_for_hour = first_employee + second_employee + third_employee
if students_for_hour > 0 and students_count > 0:
    needed_hours = ceil(students_count / students_for_hour)
    if needed_hours >= 4:
        all_hours = []
        for i in range(0, needed_hours + 1):
            all_hours.append(i)

        breaks = len(every_4th_element(all_hours, 4))
        needed_hours += breaks

    print(f"Time needed: {needed_hours}h.")

else:
    print("Time needed: 0h.")