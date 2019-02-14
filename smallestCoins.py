#! /usr/bin/env python

"""
Given a lot of coins, find the smallest amount of coins to change a coin.
eg: coins = [1, 5, 10, 20]
x = 32
output = 4
"""


def change(total, coins):
    """
    recursive solution, time consuming and maximum recursion depth exceed
    """
    if total == 0:
        return 0
    count = total
    for coin in coins:
        if total - coin >= 0:
            _count = change(total - coin, coins)
            if _count + 1 < count:
                count = _count + 1
    return count


def _change_dp(total, coins, cache):
    if total == 0:
        return 0
    count = total
    for coin in coins:
        if total - coin >= 0:
            if cache[total - coin] == -1:
                _count = _change_dp(total - coin, coins, cache)
                cache[total - coin] = _count
            else:
                _count = cache[total - coin]
            if count > _count + 1:
                count = _count + 1
    return count


def change_dp(total, coins):
    cache = [-1 for x in range(total)]
    return _change_dp(total, coins, cache)


if __name__ == "__main__":
    coins = [1, 5, 10, 20]
    total = 53
    print change(total, coins)
    # print change_dp(total, coins)
