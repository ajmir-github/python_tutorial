str_number = input("Enter a number >> ")

number = int(str_number)

print("Multiplication Table of " + str(number))
times = 1
while times <= 10:
 total = times*number
 print(str(times)+" x "+str(number)+" = "+str(total))
 times += 1

# for times in range(1, 11):
#  total = times*number
#  print(str(times)+" x "+str(number)+" = "+str(total))
 
