'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''

nums = [1,0,-1,0,-2,2]
target = 0
nums.sort()
res = []

for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i-1]:
        continue  # skip duplicate i
    for j in range(i + 1, len(nums)-1):
        if j >i+1 and nums[j] == nums[j-1]:
            continue
        left, right = j + 1, len(nums) - 1
        while left < right:
            s = nums[i]+ nums[j] + nums[left] + nums[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                res.append([nums[i],nums[j], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

print(res)