def bubbleSort(nums : []) -> []:
    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j+1] < nums[j]:
                nums[j+1] , nums[j] = nums[j] , nums[j+1]

    return nums

nums = [1,4,2,7,8,6,8,0,1,2,3,8,2,5]


print(bubbleSort(nums))