#!/usr/bin/python3
"""Island perimeter computing module.
"""


def isWinner(x, nums):
    """
    determine who the winner of each game is
    """
    if x < 1 or not nums:
        return None
    mariasWins, bensWins = 0, 0
    n = max(nums)

    def SieveOfEratosthenes(n):
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):

            # If prime[p] is not
            # changed, then it is a prime
            if (prime[p]):

                # Update all multiples of p
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1

        # Print all prime numbers
        primes = [False for i in range(n)]
        for p in range(2, n+1):
            if prime[p]:
                primes[p-1] = True
        return primes

    primes = SieveOfEratosthenes(n)
    for _, n in zip(range(x), nums):
        primesCount = len(list(filter(None, primes[0: n])))
        bensWins += primesCount % 2 == 0
        mariasWins += primesCount % 2 == 1
    if mariasWins == bensWins:
        return None
    return 'Maria' if mariasWins > bensWins else 'Ben'
