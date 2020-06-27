__author__ = "akhtar"


def inorder_recursive(node):
    """
    Recursive inorder traversal of a binary tree.

    :param BTreeNode root: The root of the tree.
    :return: nothing.
    :rtype: None
    """
    if node is None:
        return
    
    inorder_recursive(node.left)
    print(node.data, end=" ")
    inorder_recursive(node.right)


def inorder_iterative(root):
    """
    Iterative inorder traversal of a binary tree.

    :param BTreeNode root: The root of the tree.
    :return: nothing.
    :rtype: None
    """
    if root is None:
        return
    
    current = root
    stack = []
    
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif len(stack):
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right
        else:
            break


def inorder(root):
    inorder_recursive(root)
