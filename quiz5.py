def findBestPrice(rodL, prices, cutPrice, memo = None):
    if(memo == None):
        memo = {
            # stores (best price, number of cuts)
            0: (prices[0], 0),
            1: (prices[1], 0)
        }
    
    if rodL not in memo:
        maxP = -1*cutPrice
        prevCuts = 0

        for i in range(1, rodL+1):
            tmp = findBestPrice(rodL-i, prices, cutPrice, memo)

            tmpPrice = tmp[0] + prices[i]
            tmpCuts = tmp[1]

            if i < rodL:
                tmpPrice -= cutPrice

            if tmpPrice > maxP:
                maxP = tmpPrice
                if i < rodL: 
                    prevCuts = tmpCuts + 1
                else:
                    prevCuts = 0
        
        memo[rodL] = (maxP, prevCuts)
    
    return memo[rodL]



for i in range(1, 11):
    print("C = ", i, " | ", findBestPrice(10, [0, 2, 7, 12, 15, 18, 19, 23, 25, 26, 31], i))

print("C = ", 0, " | ", findBestPrice(10, [0, 2, 7, 12, 15, 18, 19, 23, 25, 26, 31], 0))
print("C = ", 100, " | ", findBestPrice(10, [0, 2, 7, 12, 15, 18, 19, 23, 25, 26, 31], 100))