from functools import lru_cache

def getLength(count):
    if count == 1:
        return 1
    return 1 + len(str(count))

def minLengthOfCompressedString(s, k):
    n = len(s)

    @lru_cache(None)
    def dp(index, prev_char, prev_count, remaining_deletes):
        if remaining_deletes < 0:
            return float('inf')
        if index == n:
            return 0

        delete_option = dp(index + 1, prev_char, prev_count, remaining_deletes - 1)

        current_char = s[index]

        if current_char == prev_char:
            add_length = 1 if prev_count in (1, 9, 99) else 0
            keep_option = add_length + dp(index + 1, prev_char, prev_count + 1, remaining_deletes)
        else:
            keep_option = 1 + dp(index + 1, current_char, 1, remaining_deletes)

        return min(delete_option, keep_option)

    return dp(0, '', 0, k)
