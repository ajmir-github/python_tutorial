# Write (x, w, a)
new_file = open("assets/data.txt", "w")
new_file.write("1-This is appended data.")
new_file.write("2-This is appended data.")
new_file.write("3-This is appended data.")
new_file.close()
print("File created and written!")

# Read (rt, tb)
file = open("assets/data.txt", "rt")

print(file.read(6))
for line in file.readlines():
 print(line)

print(file.read(10))
print(file.read(10))