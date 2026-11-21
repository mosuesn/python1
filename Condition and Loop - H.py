nums = []
for i in range(int(input())):
    nums.append(i+1)
while len(nums) > 1:
    nums.remove(int(input()))
print(nums[0])