def max_independent_set(nums):
    n = len(nums)
    dp = [0] * n
    selected = [False] * n

    # handle the base case
    if n == 0:
        return []
    if n == 1:
        return [nums[0]] if nums[0] >= 0 else []

    # calculate dp[i] as the max sum possible ending at index i
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        # dp[i-1] represents the max sum without considering nums[i]
        # dp[i-2] + nums[i] represents the max sum considering nums[i]
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    # construct the selected list
    i = n - 1
    while i >= 0:
        if dp[i] == dp[i-1]:
            i -= 1
        else:
            selected[i] = True
            i -= 2

    # return the selected numbers
    result = [nums[i] for i in range(n) if selected[i]]
    return result if result else []
