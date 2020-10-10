def intersection(arrays):
    cache = {}
    goal = len(arrays)
    result = []

    for arrIndex, arr in enumerate(arrays):
        for num in arr:
            if num not in cache:
                cache[num] = [arrIndex]
            else:
                cache[num].append(arrIndex)
                if len(cache[num]) == goal:
                    result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))