__author__ = "akhtar"


def preorder_recursive(node):
    """
    Recursive preorder traversal of a binary tree.

    :param BTreeNode root: The root of the tree.
    :return: nothing.
    :rtype: None
    """
    if node is None:
        return
    
    print(node.data, end=" ")
    preorder_recursive(node.left)
    preorder_recursive(node.right)


def preorder_iterative(root):
    """
    Iterative preorder traversal of a binary tree.

    :param BTreeNode root: The root of the tree.
    :return: nothing.
    :rtype: None
    """
    if root is None:
        return
    
    stack = []
    stack.append(root)
    
    while len(stack):
        node = stack.pop()
        print(node.data, end=" ")
        
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)


def preorder(root):
    preorder_recursive(root)
