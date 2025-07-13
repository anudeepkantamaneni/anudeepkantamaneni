def longestCommonSubsequence(s: str, t: str) -> int:
    m, n = len(s), len(t)
    
    # Initialize DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Input reading
if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    print(longestCommonSubsequence(s, t))
