from collections import deque

from tree.nodes import BTreeNode

__author__ = "akhtar"


def insert_into_binary_tree(root, data):
    """
    Insert an element into a binary tree with given root.

    :param BTreeNode root: The root of the tree.
    :param int data: The data to insert.
    :return: nothing.
    :rtype: None
    """
    queue = deque([])
    queue.append(root)
    new_node = BTreeNode(data)

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
