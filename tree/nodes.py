__author__ = "akhtar"


class BTreeNode:
    """ Node for a Binary Tree """
    
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return "Node: " + str(self.data)
    
    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left

    def set_right(self, right):
        self.left = right

    def get_right(self):
        return self.right


class NTreeNode:
    """ Node for an N-ary Tree """
    
    def __init__(self, data=None):
        self.data = data
        self.first_child = None
        self.next_sibling = None
    
    def __str__(self):
        return "Node: " + str(self.data)
    
    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_first_child(self, first_child):
        self.first_child = first_child

    def get_first_child(self):
        return self.first_child

    def set_next_sibling(self, next_sibling):
        self.next_sibling = next_sibling

    def get_next_sibling(self):
        return self.next_sibling
