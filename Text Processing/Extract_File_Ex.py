file = input().split(".")
extension = file[1]
first = file[0]
new_first = first.split("\\")
file_name = new_first[-1]
print(f"File name: {file_name}\nFile extension: {extension}")

