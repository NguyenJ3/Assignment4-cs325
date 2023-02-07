def max_independent_set(nums):
    n = len(nums) #n will be the lenght of nums 
    if n == 0 or min(nums) < 0: 
        return [] #stores elements from the if statement 
    dp = [0] * n 
    dp[0] = nums[0] #The first element that includes the max sum
    dp[1] = max(nums[0], nums[1]) #first or second element 
    
    for i in range (2,n ): #loops the elements 
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    results =  [] #stores the list of elements within max 
    i = n - 1 

    #loop through the list reversing it 

    while i >= 0: 
        if i >= 2 and dp[i-2] + nums[i] >= dp[i-1]: 
            results.append(nums[i]) # appends the element to the results 
            i = i - 2
        else: 
            i = 1 - i

    return results[:: -1 ] #returns the reverse list 