if root is None:
    return []
result = []    
q = collections.deque([root])

while len(q) != 0:
    node = q.popleft()
    # this is for binary tree
    if node.left is not None:
        q.append(node.left)
    if node.right is not None:
        q.append(node.right)
    result.append(node.value)

    # this is for n-aray tree
    # for child in node.children:
    #     q.append(child)

    return result