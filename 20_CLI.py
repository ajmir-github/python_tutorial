import sys

# print(sys.argv)
path, command, data = sys.argv
if command == "get":
 print(f"GET {data}")