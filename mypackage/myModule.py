def top_n(items, n):
    """Return the top n items in an array, in descending order.

    Args:
        items (array): list or array-like object containing numerical values.
        n (int): number of top items to return.

    Returns:
        array: top n items, in descending order.

    Examples:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 4]
    """
    for i in range(n):
        for j in range(len(items) - 1):
            if items[j] < items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    top_n = items[-n:]
    return items[::-1]