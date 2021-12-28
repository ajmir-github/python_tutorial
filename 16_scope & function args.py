# ----- Scope of if/else & functions

# x = 22
# if True:
#  x = 44

# def mut():
#  x = 55
#  print(x)

# mut()
# print(x)


# ----- Global keyword

# num = 0
# print(num)

# def increment():
#  global num
#  num += 1
#  print(num)

# increment()
# print(num)


# ----- passing lambda function as a parameter

# sum = lambda  x,y: x + y
# subtract = lambda x, y: x - y

# def math(a, b, fun):
#  return fun(a, b + 10)

# print(math(2, 3, subtract))


# ----- returning lambda function

# def compute(a, b):
#  return lambda x: a*x + b*x

# d = compute(2, 4)
# a = d(10)
# print(a)

# ----- empty function
# def skip():
#  pass

# skip()
# print("done")


# ----- Function **kwargs and *args
# def log(**kwargs):
#  print(kwargs)

# log(name="Ahmad", age=22)

# def sum(*args):
#  total = 0
#  for num in args:
#   total += num
#  return total


# total = sum(2, 6, 6)
# print(total)
