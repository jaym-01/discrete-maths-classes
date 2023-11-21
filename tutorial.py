def dc_bs(A, x):
    if len(A) <= 1:
        if len(A) == 1 and A[0] == x:
            return 0
        return -1

    mid = len(A) // 2

    if(A[mid] == x):
        return mid
    elif(A[mid] > x):
        return dc_bs(A[:mid], x)
    else:
        return mid + 1 + dc_bs(A[mid + 1:], x)

def bs_nr(A, x):
    
    start = 0
    end = len(A) - 1

    while(start <= end):
        mid = (start + end)//2

        if A[mid] == x:
            return mid
        elif A[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    
inp = [6, 50, 9, 70, 42, 84, 73, 77, 67, 20, 19, 5, 30, 63, 27, 16, 79, 96, 44, 69, 57, 2, 98, 87, 11, 36, 88, 37, 61, 53, 75, 31, 43, 94, 33, 29, 52, 3]
inp = sorted(inp)
print(inp)
print(bs_nr(inp, 70))