def max_independent_set(nums):
    n = len(nums) #n will be the lenght of nums 
    if n == 0 or min(nums) < 0: 
        return [] #stores elements from the if statement 
    dp = [0] * n 
    dp[0] = nums[0] #The first element that includes the max sum
    dp[1] = max(nums[0], nums[1]) #first or second element 
    