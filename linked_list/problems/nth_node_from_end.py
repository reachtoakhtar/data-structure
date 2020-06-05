from linked_list.exception import EmptyListError, RangeError

__author__ = "akhtar"


def nth_node_from_end(linked_list, n):
    """
    Finds nth node from end of a linked list (assume positions as 1 based).
    Hint: For a linked list of size m, nth node from end would be
    (m - n + 1)th node from beginning.

    :param SingleLinkedList linked_list: The person sending the message.
    :param int n: The position from end.
    :return: the data of the node.
    :rtype: int
    :raises EmptyListError: if the list is empty.
    :raises RangeError: if length of list < n < 0.
    """

    list_length = linked_list.get_length()
    if list_length == 0:
        raise EmptyListError("List is empty, can't find node")

    if not (1 <= n <= list_length):
        raise RangeError("Position range must be 1 through {0}".format(list_length))

    nth_from_end = list_length - n + 1
    pointer = linked_list.head
    position = 1

    while position != nth_from_end:
        pointer = pointer.get_next()
        position += 1

    return pointer.data


def nth_node_from_end_single_scan(linked_list, n):
    """
    Finds nth node from end of a linked list (assume positions as 1 based).
    Hint: For a linked list of size m, nth node from end would be
    (m - n + 1)th node from beginning.

    :param SingleLinkedList linked_list: The person sending the message.
    :param int n: The position from end.
    :return: the data of the node.
    :rtype: int
    :raises EmptyListError: if the list is empty.
    :raises RangeError: if length of list < n < 0.
    """

    list_length = linked_list.get_length()
    if list_length == 0:
        raise EmptyListError("List is empty, can't find node")

    if not (1 <= n <= list_length):
        raise RangeError("Position range must be 1 through {0}".format(list_length))

    pointer = linked_list.head
    temp = linked_list.head
    position = 1

    while temp.get_next():
        if position == n:
            temp = temp.get_next()
            pointer = pointer.get_next()
        else:
            temp = temp.get_next()
            position += 1

    return pointer.data
