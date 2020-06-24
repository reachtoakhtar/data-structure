__author__ = "akhtar"


def level_with_maximum_sum(root):
    """
    Find the level with maximum sum in a binary tree.

    :param TreeNode root: The root of the tree.
    :return: the level with maximum sum and the sum.
    :rtype: tuple
    """
    if root is None:
        return
    
    stack = [root]
    level = 1
    
    max_sum = root.data
    max_sum_level = 1
    
    while len(stack):
        current_level_sum = 0
        next_level_nodes = []
        
        for _ in range(len(stack)):
            node = stack.pop()
            current_level_sum += node.data
            
            if node.left:
                next_level_nodes.append(node.left)
        
            if node.right:
                next_level_nodes.append(node.right)
        
        if current_level_sum > max_sum:
            max_sum = current_level_sum
            max_sum_level = level
        
        level += 1
        stack = next_level_nodes
    
    return max_sum_level, max_sum

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#
#
# def level_with_maximum_sum(root):
#     """
#     Find the level with maximum sum in a binary tree.
#
#     :param TreeNode root: The root of the tree.
#     :return: the level with maximum sum.
#     :rtype: int
#     """
#
#     # used for storing each level sum
#     d = {}
#
#     stack = [root]
#
#     # determining current level of tree
#     level = 1
#
#     while stack:
#         next_lvl_nodes = []
#         current_lvl_sum = 0
#
#         for i in range(len(stack)):
#             node = stack.pop()
#
#             # sum each nodes value
#             current_lvl_sum += node.val
#
#             # check for children
#             if node.left:
#                 next_lvl_nodes.append(node.left)
#             if node.right:
#                 next_lvl_nodes.append(node.right)
#
#         d[level] = current_lvl_sum
#         level += 1
#         stack = next_lvl_nodes
#
#     # Get key(level) of maximum value in dictionary
#     return max(d, key=d.get)
