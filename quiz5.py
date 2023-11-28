memo = None

# show where the cuts are made
def helper(rodL, prices, cutPrice, mem):
    if(mem == None):
        mem = {
            # stores (best price, cut position)
            0: (prices[0], 0),
            1: (prices[1], 0)
        }
    
    if rodL not in mem:
        maxP = -1*cutPrice
        cutPos = 0

        for i in range(1, rodL+1):
            tmp = helper(rodL-i, prices, cutPrice, memo)

            tmpPrice = tmp[0] + prices[i]

            if i < rodL:
                tmpPrice -= cutPrice

            if tmpPrice > maxP:
                maxP = tmpPrice
                cutPos = i
                
        
        mem[rodL] = (maxP, cutPos)
    
    return mem[rodL]

def findBestPrice(rodL, prices, cutPrice):
    memo = None

    tmp = helper(rodL, prices, cutPrice, memo)

    price = tmp[0]
    cutPos = tmp[1]

    cutPoss = []
    currLen = rodL

    while(cutPos > 0):
        cutPoss.append(cutPos)
        tmp = cutPos
        cutPos -= memo[currLen - cutPos][1]
        currLen = currLen - tmp

    return (price, cutPoss) 
    


for i in range(1, 11):
    print("C = ", i, " | ", findBestPrice(10, [0, 2, 7, 12, 15, 18, 19, 23, 25, 26, 31], i))

print("C = ", 0, " | ", findBestPrice(10, [0, 2, 7, 12, 15, 18, 19, 23, 25, 26, 31], 0))
print("C = ", 100, " | ", findBestPrice(10, [0, 2, 7, 12, 15, 18, 19, 23, 25, 26, 31], 100))