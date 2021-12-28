nums = [3, 4, 5, 6, 7]
for x in nums:
 print(x)

for num in range(20):
 print(num+1)

for n in range(10, 20):
 print(n)


nums = []
for n in range(10, 21):
 nums.append(n)

nums.reverse()

for n in nums:
 print(n)


nums = [3, 4, 5, 6, 7]
print(nums)

length = len(nums)
index = 0
while index < length:
 nums[index] *= 10
 index += 1

print(nums)


nums = [3, 4, 5, 6, 7]
print(nums)

for index, num in enumerate(nums):
 nums[index] += 2

print(nums)