if root is None:
    return

def dfs(node):
    # Base case: leaf node
    if node.left is None and node.right is None:
        # Base case answer generated here

    # Recursive Case: Internal Node
    if node.left is not None:
        dfs(node.left)
    if node.right is not None:
        dfs(node.right)

dfs(root)