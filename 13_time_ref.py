import time

print(time.time())
print(time.asctime())
print(time.gmtime().tm_mday)
print(time.localtime().tm_hour)

print("A")
time.sleep(5)
print("B")

def loop_fun(r):
 nums = []
 for num in range(r):
  nums.append(num)


starting_time = time.time()
loop_fun(10000000)
ending_time = time.time()
duration = ending_time - starting_time
print(duration)
