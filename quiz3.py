def dcSearch(X, target):
    if(len(X) == 1):
        if(X[0] == target):
            return 0
        else:
            return -1
        
    mid = len(X) // 2

    if(X[mid] > target):
        return dcSearch(X[:mid], target)
    else:
        return mid + dcSearch(X[mid:], target)
    
test = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(10):
    print(dcSearch(test, i))