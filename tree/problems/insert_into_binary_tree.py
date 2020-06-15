from collections import deque

from tree.binary_tree import TreeNode

__author__ = "akhtar"


def insert_into_binary_tree(node, data):
    queue = deque([])
    queue.append(node)
    new_node = TreeNode(data)

    # Do level order traversal until we find an empty place.
    while len(queue):
        node = queue.popleft()

        if node.left is None:
            node.left = new_node
            break
        else:
            queue.append(node.left)

        if node.right is None:
            node.right = new_node
            break
        else:
            queue.append(node.right)
