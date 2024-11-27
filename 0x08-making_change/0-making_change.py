#!/usr/bin/python3
"""module doc"""


def makeChange(coins, total):
    # Memoization cache
    memo = {}

    def dp(remaining):
        # Base cases
        if remaining < 0:
            return -1
        if remaining == 0:
            return 0

        # Check if result is already memoized
        if remaining in memo:
            return memo[remaining]

        # Initialize min coins to a large value
        min_coins = float('inf')

        # Try each coin
        for coin in coins:
            result = dp(remaining - coin)
            if result != -1:
                min_coins = min(min_coins, result + 1)

        # Store and return result
        memo[remaining] = min_coins if min_coins != float('inf') else -1
        return memo[remaining]

    return dp(total)
