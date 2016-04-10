def insert_in_order(L, i, unique=True):
    """
    Insert i into `L` in order with or without duplicates
    """
    for index in xrange(len(L)):
        if unique and L[index] == i:
            return
        if L[index] > i:
            L.insert(index, i)
            return
    L.append(i)
