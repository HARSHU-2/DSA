# Traversals in BST
class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data, end=" ")
        printInorder(root.right)


if __name__ == "__main__":
    # Build the tree
    root = Node(100)
    root.left = Node(20)
    root.right = Node(200)
    root.left.left = Node(10)
    root.left.right = Node(30)
    root.right.left = Node(150)
    root.right.right = Node(300)

    print("Inorder Traversal:", end=" ")
    printInorder(root)