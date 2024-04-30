class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

# Function to find descendants of a node
def find_descendants(node):
    descendants = []
    
    # Recursive function to traverse the tree
    def dfs(node):
        if node:
            descendants.append(node.val)
            for child in node.children:
                dfs(child)
    
    dfs(node)
    # Exclude the given node itself from the list of descendants
    return descendants[1:]

# Example usage
root = TreeNode(1)
root.children = [TreeNode(2), TreeNode(3)]
root.children[0].children = [TreeNode(4), TreeNode(5)]
root.children[1].children = [TreeNode(6), TreeNode(7)]

# Find descendants of node with value 2
node_3 = root.children[0]
descendants_2 = find_descendants(node_3)
print("Descendants of node with value 2:", descendants_2)
