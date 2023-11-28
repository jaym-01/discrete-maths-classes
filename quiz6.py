import sys

def greedy(n, coins):
    current_coin = len(coins) - 1

    count = 0

    while(n > 0):
        if(n - coins[current_coin] >= 0):
            n -= coins[current_coin]
            count += 1
        else:
            current_coin -= 1

    return count

mem = {}
def dynamic(n, coins):
    if n == 0:
        return 0

    if(n in mem):
        return mem[n]
    
    min = sys.maxsize

    for coin in coins:
        if coin <= n:
            coinsUsed = dynamic(n - coin, coins) + 1
            if(coinsUsed < min):
                min = coinsUsed

    mem[n] = min

    return mem[n]


coinsArr = [
    [1, 2, 5, 11, 23, 97],
    [1, 2, 3, 4, 11, 31, 79],
    [1, 4, 24, 57, 88, 93],
    [1, 35, 36, 56, 72, 84, 100],
    [1, 8, 35, 36, 43, 74],
    [1, 2, 4, 8, 18, 53],
    [1, 2, 34, 40, 45, 57, 73],
    [1, 2, 3, 6, 12, 18, 64]
]

# print(dynamic(3, coinsArr[1]))

for coinset in coinsArr:
    mem = {}
    for i in range(1, 2*coinset[len(coinset) - 1]):
        dyna = dynamic(i, coinset)
        gre = greedy(i, coinset)

        if(dyna != gre):
            print(dyna, " || ", gre)
            print("This is not canonical, failed on ", i, " : ", coinset)
            break