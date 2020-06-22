__author__ = "akhtar"


def height(root, ans):
    if root is None:
        return 0
    
    left_height = height(root.left, ans)
    right_height = height(root.right, ans)
    
    # update the answer, because diameter of a tree is nothing but maximum
    # value of (left_height + right_height + 1) for each node
    ans[0] = max(ans[0], 1 + left_height + right_height)
    
    return 1 + max(left_height, right_height)


def find_diameter(root):
    """
    Find the diameter of a binary tree with given root.

    :param TreeNode root: The root of the tree.
    :return: the diameter of the tree.
    :rtype: int
    """
    if root is None:
        return 0

    # This will store the final answer
    ans = [-1]
    
    height(root, ans)
    return ans[0]
