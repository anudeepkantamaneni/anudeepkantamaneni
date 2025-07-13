from typing import List

def is_possible(arr: List[int], n: int, m: int, max_pages: int) -> bool:
    student_count = 1
    pages_sum = 0

    for pages in arr:
        if pages > max_pages:
            return False
        if pages_sum + pages > max_pages:
            student_count += 1
            pages_sum = pages
            if student_count > m:
                return False
        else:
            pages_sum += pages

    return True

def findPages(arr: List[int], n: int, m: int) -> int:
    if m > n:
        return -1

    low = max(arr)
    high = sum(arr)
    result = high

    while low <= high:
        mid = (low + high) // 2
        if is_possible(arr, n, m, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result
