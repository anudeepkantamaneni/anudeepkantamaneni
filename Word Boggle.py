def findPossibleWord(arr, mat):
    from collections import defaultdict
    n, m = len(mat), len(mat[0])
    found_words = set()

    # All 8 directions
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]

    def dfs(i, j, word, index, visited):
        if index == len(word):
            return True
        if not (0 <= i < n and 0 <= j < m) or visited[i][j] or mat[i][j] != word[index]:
            return False

        visited[i][j] = True
        for dx, dy in directions:
            if dfs(i + dx, j + dy, word, index + 1, visited):
                visited[i][j] = False
                return True
        visited[i][j] = False
        return False

    for word in arr:
        found = False
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0]:
                    visited = [[False]*m for _ in range(n)]
                    if dfs(i, j, word, 0, visited):
                        found_words.add(word)
                        found = True
                        break
            if found:
                break

    return sorted(found_words)
