def insert_in_order(L, item, unique=True):
    """
    Insert i into `L` in order with or without duplicates
    :param L: list to add to
    :param item: item to insert
    :param unique: if true, do not add duplicates
    """
    for index in xrange(len(L)):
        if unique and L[index] == item:
            return
        if L[index] > item:
            L.insert(index, item)
            return
    L.append(item)
