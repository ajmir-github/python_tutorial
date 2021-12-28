# i = 1
# while i <= 10:
#  print("i: " + str(i))
#  i = i+1


# i = 0
# while True:
#  print(i)
#  i = i+1
#  if i == 19:
#   break


# i = 0
# while i < 10:
#  i = i+1

#  if i < 5:
#   print("before continue")
#   continue
#   print("after continue")
#  else:
#   print(i)


# list_nums = [11, 22, 33, 44, 55, 66, 77]
# length = len(list_nums)
# i = 0

# while i < length:
#  print(list_nums[i])
#  i = i+1


list_nums = [11, 22, 33, 44, 55, 66]
length = len(list_nums)

index = length
while True:
 index = index-1
 if index < 0:
  break
 print(list_nums[index])
