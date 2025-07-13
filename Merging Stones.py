def mergeStones(stones, K):
    n = len(stones)
    if (n - 1) % (K - 1) != 0:
        return -1

    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + stones[i]

    import math
    dp = [[0] * n for _ in range(n)]

    for length in range(K, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = math.inf
            for mid in range(i, j, K - 1):
                dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j])
            if (length - 1) % (K - 1) == 0:
                dp[i][j] += prefix_sum[j + 1] - prefix_sum[i]

    return dp[0][n - 1]
