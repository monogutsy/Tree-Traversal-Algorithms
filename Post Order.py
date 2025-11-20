class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=", ")

root = TreeNode('S')
nodeA = TreeNode('B')
nodeB = TreeNode('D')
nodeC = TreeNode('C')
nodeD = TreeNode('A')
nodeE = TreeNode('G')
nodeF = TreeNode('F')
nodeG = TreeNode('E')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Traverse
postOrderTraversal(root)
