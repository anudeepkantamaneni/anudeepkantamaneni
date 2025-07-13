def maxSubarraySum(arr):
    max_so_far = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_so_far = max(max_so_far, current_sum)

    return max_so_far

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(maxSubarraySum(arr))
