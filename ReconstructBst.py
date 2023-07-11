# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    if len(preOrderTraversalValues) == 0:
        return None

    root = preOrderTraversalValues[0]
    rootBst = BST(root)
    rightSubRootIndex = len(preOrderTraversalValues)

    for i in range (1, len(preOrderTraversalValues)):
        if preOrderTraversalValues[i] >= root:
            rightSubRootIndex = i
            break

    leftSubTree = reconstructBst(preOrderTraversalValues[1:rightSubRootIndex])
    rightSubTree = reconstructBst(preOrderTraversalValues[rightSubRootIndex:])

    return BST(root, leftSubTree, rightSubTree)
