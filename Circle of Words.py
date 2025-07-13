from collections import defaultdict

def circleOfWords(words):
    graph = defaultdict(list)
    in_deg = defaultdict(int)
    out_deg = defaultdict(int)
    letters = set()

    for word in words:
        start = word[0]
        end = word[-1]
        graph[start].append(end)
        out_deg[start] += 1
        in_deg[end] += 1
        letters.update([start, end])

    for ch in letters:
        if in_deg[ch] != out_deg[ch]:
            return False

    # DFS to check connectivity
    def dfs(node, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)

    # Start from any letter that has an edge
    start_node = next(iter(graph))
    visited = set()
    dfs(start_node, visited)

    for ch in letters:
        if ch not in visited:
            return False

    return True
