def findArrayIntersection(arr, n, brr, m):
    i = j = 0
    result = []

    while i < n and j < m:
        if arr[i] == brr[j]:
            result.append(arr[i])
            i += 1
            j += 1
        elif arr[i] < brr[j]:
            i += 1
        else:
            j += 1

    return result if result else [-1]
