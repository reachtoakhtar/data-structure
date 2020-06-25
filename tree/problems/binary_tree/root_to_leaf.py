__author__ = "akhtar"


def all_paths_from_root_to_leaf(node, path=[]):
    """
    Print all paths from root to leaf in a binary tree.

    :param TreeNode node: A node of the tree.
    :return: nothing.
    :rtype: None
    """
    if node is None:
        return
    
    path.append(node.data)
    
    if node.left is None and node.right is None:
        print(path)
        
    all_paths_from_root_to_leaf(node.left, path)
    all_paths_from_root_to_leaf(node.right, path)
    path.pop()
