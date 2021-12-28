nums = [1, 2, 3, 4, 5, 6]
print(nums)
print(nums[0])
print(nums[2])
print(nums[-1])
print(len(nums))

print(3 in nums)
print(7 in nums)

nums.append(7)
nums.insert(2, 2.5)
nums.insert(0, 100)
print(nums)

nums = [1, 2, 3, 4, 5, 6]
nums.remove(1)
nums.pop()
nums.clear()
print(nums)


nums = [1, 2, 3, 4, 5, 6, 11, 11, 22]
print(nums.count(12))
print(nums.index(6))
nums.reverse()

nums = [1, 4, 5, 6, 2, 3]
print(nums)

nums.sort()
print(nums)
