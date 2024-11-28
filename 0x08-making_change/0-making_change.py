#!/usr/bin/python3
"""module doc"""


def makeChange(coins, total):
    memo = {}

    def dfs(total):
        if total == 0:
            return 0
        if total in memo:
            return memo[total]

        res = 1e9
        for coin in coins:
            if total - coin >= 0:
                res = min(res, 1 + dfs(total - coin))
            
        memo[total] = res
        return res
    
    minCoins = dfs(total)
    return -1 if minCoins >= 1e9 else minCoins