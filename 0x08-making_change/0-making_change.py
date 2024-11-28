#!/usr/bin/python3
"""module doc"""


def makeChange(coins, total):
    # Check for invalid inputs
    if total < 0 or not coins:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for a in range(1, total + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[total] if dp[total] != total + 1 else -1
