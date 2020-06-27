__author__ = "akhtar"

from collections import deque


def _delete_deepest(root, d_node):
    q = deque([])
    q.append(root)
    
    while len(q):
        temp = q.popleft()
        
        if temp is d_node:
            temp = None
            return
        
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)
        
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)


def delete_node(root, data):
    """
    Delete a node from a binary tree with given root.

    :param BTreeNode root: The root of the tree.
    :param int data: The node data to delete.
    :return: nothing.
    :rtype: None
    
    Steps:
    1. Starting at root, find the deepest and rightmost node in binary tree and
     the node which we want to delete.
    2. Replace the deepest rightmost node’s data with the node to be deleted.
    3. Then delete the deepest rightmost node.
    """
    if root is None:
        return None
    
    if root.left is None and root.right is None:
        if root.data == data:
            return None
        else:
            return
    
    data_node = None
    q = deque([])
    q.append(root)
    
    temp = None
    while len(q):
        temp = q.popleft()
        
        if temp.data == data:
            data_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    
    if data_node:
        data = temp.data
        _delete_deepest(root, temp)
        data_node.data = data
