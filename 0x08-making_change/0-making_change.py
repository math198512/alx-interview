#!/usr/bin/python3
"""module doc"""


def makeChange(coins, total):
    # Check for invalid inputs
    if total < 0 or not coins:
        return -1
    
    # Use dynamic programming with bottom-up approach
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1
