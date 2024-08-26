dp = [0,1]
'''
min(dp[] + coin[], 
dp[11] -> min(1 + DP[10], 2 + DP[9], 5 + DP[6])
'''
def thing(coins,amount):
    dp = [0] * (amount + 1)
    for curamount in range(1, amount + 1):
        combinations = []
        for coin in coins:
            newamount = curamount - coin
            if newamount >= 0 and dp[newamount] != -1:
                combinations.append(dp[newamount])
        if not combinations:
            dp[curamount] = -1
            continue
        dp[curamount] = min(combinations) + 1
    print(dp)
    return dp[amount]
thing([1,2,5],11)