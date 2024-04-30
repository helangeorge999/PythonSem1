class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

# Function to perform DFS traversal to find level, ancestors, descendants, and internal vertices
def dfs(node, level, ancestors):
    if node:
        print("Node:", node.val, "Level:", level, "Ancestors:", ancestors)
        for child in node.children:
            dfs(child, level + 1, ancestors + [node.val])

# Example usage
root = TreeNode(1)
root.children = [TreeNode(2), TreeNode(3)]
root.children[0].children = [TreeNode(4), TreeNode(5)]
root.children[1].children = [TreeNode(6), TreeNode(7)]

# Find properties using DFS
print("Finding properties using DFS:")
dfs(root, 0, [])

