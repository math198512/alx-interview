#!/usr/bin/python3
"""module doc"""


def makeChange(coins, total):
    # Handle base cases
    if total < 0 or total == 0:
        return 0

    # Initialize DP array with large values (representing impossibility)
    # We use total + 1 as a "large" value that indicates impossibility
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # 0 coins needed to make 0 total

    # Iterate through all possible totals from 1 to target total
    for i in range(1, total + 1):
        # Try each coin denomination
        for coin in coins:
            # If coin is less than or equal to current total
            if coin <= i:
                # Update minimum coins needed
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return result, using -1 if no solution found
    return dp[total] if dp[total] <= total else -1
