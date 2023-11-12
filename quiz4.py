def bool_sort(x):
    ta = []
    fa = []

    for e in x:
        if(e):
            ta.append(e)
        else:
            fa.append(e)
    
    return fa + ta

print(bool_sort([False, False, True, False, True]))