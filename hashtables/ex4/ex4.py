def has_negatives(a):
    cache = {}
    result = []

    for num in a:
        absNum = abs(num)
        if absNum in cache:
            result.append(absNum)
        else:
            cache[absNum] = absNum
    print(cache)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
