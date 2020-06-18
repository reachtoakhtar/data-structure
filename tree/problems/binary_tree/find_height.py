__author__ = "akhtar"


def find_height_recursive(node):
    if node is None:
        return 0
    
    left_height = find_height_recursive(node.left)
    right_height = find_height_recursive(node.right)
    return max(left_height, right_height) + 1
