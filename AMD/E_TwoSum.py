'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
nums = [2,7,11,15]
target = 9

def TwoSum(nums, target):
    # This list will store the pair of indices where the numbers add up to the target
    pos = []

    # Initialize two pointers: one at the beginning, one at the end
    start = 0
    end = len(nums) - 1

    # Loop until the two pointers meet
    while start < end:
        current_sum = nums[start] + nums[end]

        # If the sum of the two numbers equals the target
        if current_sum == target:
            # Save the pair of indices to the result list
            pos.append((start, end))
            # Move both pointers inward to continue searching
            start += 1
            end -= 1

        # If the sum is less than the target, move the start pointer to the right
        elif current_sum < target:
            start += 1

        # If the sum is greater than the target, move the end pointer to the left
        else:
            end -= 1

    # Return the list of index pairs that match the target sum
    return pos

print(TwoSum(nums, target))
