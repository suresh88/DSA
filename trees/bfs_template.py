q = collections.deque([root])

while len(q) != 0:
    node = q.popleft()
    if node.left is not None:
        q.push(node.left)
    if node.right is not None:
        q.push(node.right)