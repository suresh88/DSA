from collections import deque

def bfs(root):
    if root is None:
        return []
    result = []    
    q = deque([root])

    while len(q) != 0:
        numnodes = len(q)
        temp = []
        for _ in range(numnodes):
            node = q.popleft()
            # this is for binary tree
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            temp.append(node.value)

        result.append(temp)

        # this is for n-aray tree
        # for child in node.children:
        #     q.append(child)

    return result