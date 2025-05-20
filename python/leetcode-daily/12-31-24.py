def mincostTickets(days, costs):
    n = len(days)
    dp = [0] * (days[-1] + 1)
    day_set = set(days)
    
    for i in range(1, days[-1] + 1):
        if i not in day_set:
            dp[i] = dp[i - 1]
        else:
            dp[i] = min(dp[i - 1] + costs[0], 
                        dp[max(0, i - 7)] + costs[1], 
                        dp[max(0, i - 30)] + costs[2])
    
    return dp[days[-1]]

# Example usage:
days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
print(mincostTickets(days, costs))  # Output: 11