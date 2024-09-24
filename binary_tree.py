class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Task 1: In-order Traversal
def in_order_traversal(root):
    if root:
        # Traverse the left subtree
        in_order_traversal(root.left)
        # Visit the node
        print(root.val, end=' ')
        # Traverse the right subtree
        in_order_traversal(root.right)

# Task 2: Pre-order Traversal
def pre_order_traversal(root):
    if root:
        # Visit the node
        print(root.val, end=' ')
        # Traverse the left subtree
        pre_order_traversal(root.left)
        # Traverse the right subtree
        pre_order_traversal(root.right)

# Task 3: Post-order Traversal
def post_order_traversal(root):
    if root:
        # Traverse the left subtree
        post_order_traversal(root.left)
        # Traverse the right subtree
        post_order_traversal(root.right)
        # Visit the node
        print(root.val, end=' ')

# Task 4: Testing the Traversal Algorithms
if __name__ == "__main__":
    # Create the binary tree
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(40)
    root.left.right = Node(20)
    root.right.left = Node(60)
    root.right.right = Node(80)

    # Test In-order Traversal
    print("In-order Traversal:")
    in_order_traversal(root)  # Expected output: 40 30 20 50 60 70 80
    print("\n")

    # Test Pre-order Traversal
    print("Pre-order Traversal:")
    pre_order_traversal(root)  # Expected output: 50 30 40 20 70 60 80
    print("\n")

    # Test Post-order Traversal
    print("Post-order Traversal:")
    post_order_traversal(root)  # Expected output: 40 20 30 60 80 70 50
    print("\n")
