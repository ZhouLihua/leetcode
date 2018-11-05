#! /usr/bin/env python


def coin_changes_dp(coins, total, index, memo):
    # if there is no coin need to change,
    # no solution exists
    if total < 0:
        return 0

    # if total is o, then only 1 solution
    if total == 0:
        return 1

    # there are no coins and total is greater then 0,
    # then no solution
    if index <= 0 and total > 0:
        return 0

    key = "-".join([str(total), str(index)])
    if key in memo.keys():
        return memo.get(key)
    count = coin_changes_dp(coins, total, index-1, memo) + coin_changes_dp(coins, total - coins[index - 1], index, memo)
    memo[key] = count
    return count


def coin_changes(coins, total, index):
    # if there is no coin need to change,
    # no solution exists
    if total < 0:
        return 0

    # if total is o, then only 1 solution
    if total == 0:
        return 1

    # there are no coins and total is greater then 0,
    # then no solution
    if index <= 0 and total > 0:
        return 0

    return coin_changes(coins, total, index-1) + coin_changes(coins, total - coins[index - 1], index)


def coin_change_helper(coins, total):
    memo = dict()
    return coin_changes_dp(coins, total, len(coins), memo)


if __name__ == "__main__":
    coins_ = [1, 2, 3]

    print(coin_change_helper(coins_, 800))
    # this is much slower
    print(coin_changes(coins_, 800, len(coins_)))
