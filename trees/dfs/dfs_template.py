if root is None:
    return

def dfs(node):
    if node.left is not None:
        dfs(node.left)
    if node.right is not None:
        dfs(node.right)

dfs(root)