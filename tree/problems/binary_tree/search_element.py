from collections import deque

__author__ = "akhtar"


def find_element_recursive(node, element):
    """
    Find the given element in a binary tree.

    :param BTreeNode node: The root of the tree.
    :param int element: The element to be searched.
    :return: true if the element is found else false.
    :rtype: bool
    """
    if node is None:
        return False

    if node.data == element:
        return True

    temp = find_element_recursive(node.left, element)
    if temp:
        return temp
    else:
        return find_element_recursive(node.right, element)


def find_element_iterative(root, element):
    """
    Find the given element in a binary tree.

    :param BTreeNode root: The root of the tree.
    :param int element: The element to be searched.
    :return: true if the element is found else false.
    :rtype: bool
    """
    if root is None:
        return False
    
    queue = deque([])
    queue.append(root)
    
    while len(queue):
        node = queue.popleft()
        if node.data == element:
            return True
        
        if node.left is not None:
            queue.append(node.left)
        
        if node.right is not None:
            queue.append(node.right)
        
    return False
