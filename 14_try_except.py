x = 4
y = 5


try:
 # print(x + y)
 print("Number: " + x)
except NameError:
 print("NameError")
except TypeError:
 print("TypeError")

print("next")


try:
 print("try")
except:
 print("Error")
finally:
 print("finally")