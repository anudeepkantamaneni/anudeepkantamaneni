def traverseBoundary(root):
    if not root:
        return []

    result = []

    def isLeaf(node):
        return not node.left and not node.right

    def addLeftBoundary(node):
        curr = node.left
        while curr:
            if not isLeaf(curr):
                result.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

    def addLeaves(node):
        if isLeaf(node):
            result.append(node.data)
            return
        if node.left:
            addLeaves(node.left)
        if node.right:
            addLeaves(node.right)

    def addRightBoundary(node):
        curr = node.right
        stack = []
        while curr:
            if not isLeaf(curr):
                stack.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        while stack:
            result.append(stack.pop())

    if not isLeaf(root):
        result.append(root.data)
    addLeftBoundary(root)
    addLeaves(root)
    addRightBoundary(root)

    return result
