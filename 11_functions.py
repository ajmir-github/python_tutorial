# creating a function
def log():
 print("I am info.")

# calling a function
log()

# Parameters
def log_name(name):
 print("My name is " + name)

log_name("Khan")


# Default Parameter Value
def log_name(name = "Unknown"):
 print("My name is " + name)

log_name()

# Return Values
def sum(a, b):
 return a + b

z = sum(3, 4)
print(z)
print(sum(7, 6))

# Scope
def squre(x):
 z = 99
 number = x * x
 print(number)

print(z)
squre(3)



# say_hi(name) => Hi name, How are you?
def say_hi(name):
 print("Hi "+name+", How are you?")

# get_username() => What is your name?
def get_username():
 name = input("What is you name? ")
 return name

u_name = get_username()
say_hi(u_name)

# get_GPA(percentage) => 3.2
def get_GPA(percentage):
 return percentage/20 - 1

print(get_GPA(84))

# SumOf_list([1, 2, 3]) => 6
def sumOf_list(nums):
 total = 0
 for num in nums:
  total += num
 return total

print(sumOf_list([1, 2, 3, 4]))

# SquareOf_list([2, 4]) => [4, 16]
def squareOf_list(nums):
 new_nums = []
 for num in nums:
  x = num * num
  new_nums.append(x)
 return new_nums

print(squareOf_list([2, 4, 3]))

# filter_list([1, 2, 3, 4]) => [2, 4]
def filter_list(nums):
 new_nums = []
 for num in nums:
  if num%2 == 0:
   new_nums.append(num)
 return new_nums

x = filter_list([1, 2, 3, 4, 5, 6])
print(x)