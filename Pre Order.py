class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

root = TreeNode('S')
nodeA = TreeNode('B')
nodeB = TreeNode('D')
nodeC = TreeNode('C')
nodeD = TreeNode('A')
nodeE = TreeNode('G')
nodeF = TreeNode('F')
nodeG = TreeNode('F')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Traverse
preOrderTraversal(root)