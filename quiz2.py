def unique_items(X):
    items = {}
    U = []

    for x in X:
        if x in items:
            continue
        else:
            U.append(x)
            items[x] = 1

    return U

print(unique_items([1, 1, 2, 34, 5,6,3 ,2, 4, 5,3]))