# Boolean
has_error = True
print(has_error)

a_and = True and True
b_and = True and False
c_and = False and False
print(a_and, b_and, c_and)

a_or = True or True
b_or = True or False
c_or = False or False
print(a_or, b_or, c_or)


a = 10
b = 5
x = a > b
y = a < b
z = a == b
print(type(x))


a = 5
b = 5
c = 10
if a == b and a > c:
 print("OK")

print("Second")