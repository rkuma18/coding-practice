def divideArray(nums, k):
    def newsort(nums):
        n = len(nums)
        for i in range(n):
            for j in range(0,n-i-1):
                if nums[j] > nums[j+1]:
                   nums[j], nums[j + 1] = nums[j + 1], nums[j] 
        
        return nums
    nums = newsort(nums)
    group_size = 3
    groups = []
    for i in range(0, len(nums), group_size):
        group = nums[i:i + group_size]
        groups.append(group)
    
    for group in groups:
        if max(group) - min(group) > k:
            return []
    
    return groups

print(divideArray([1, 3, 4, 8, 7, 9, 3, 5, 1], 2))
