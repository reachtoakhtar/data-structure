__author__ = "akhtar"


def postorder_recursive(node):
    """
    Recursive postorder traversal of a binary tree.

    :param BTreeNode root: The root of the tree.
    :return: nothing.
    :rtype: None
    """
    if node is None:
        return
    
    postorder_recursive(node.left)
    postorder_recursive(node.right)
    print(node.data, end=" ")


def postorder_iterative(root):
    """
    Iterative postorder traversal of a binary tree.

    :param BTreeNode root: The root of the tree.
    :return: nothing.
    :rtype: None
    """
    if root is None:
        return
    
    stack1 = []
    stack2 = []
    stack1.append(root)
    
    while len(stack1):
        node = stack1.pop()
        stack2.append(node)
        
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    
    while len(stack2):
        node = stack2.pop()
        print(node.data, end=" ")


def postorder(root):
    postorder_recursive(root)
