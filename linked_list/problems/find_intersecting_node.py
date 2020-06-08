from linked_list.exception import EmptyListError, RangeError

__author__ = "akhtar"


def intersecting_node(list1, list2):
    """
    Suppose there are two linked lists of lengths l1 and l2,
    both of which intersect at some point and become a single linked list.
    The head of both linked lists are known. The intersecting node of the
    lists is not known. The number of nodes in each list before intersecting
    and the lengths of the lists are also unknown. Find the intersecting node.

    :param SingleLinkedList list1: The first linked linked.
    :param SingleLinkedList list2: The second linked list.
    :return: the data of the intersecting node.
    :rtype: int
    :raises EmptyListError: if the list is empty.
    """

    if list1 is None or list2 is None:
        raise EmptyListError(
            "List(s) is/are empty, can't find intersecting node")

    l1 = list1.get_length()
    l2 = list2.get_length()

    pointer1 = list1.head
    pointer2 = list2.head

    d = l1 - l2
    if l1 < l2:
        d = l2 - l1
        pointer1 = list2.head
        pointer2 = list1.head

    for i in range(d):
        pointer1 = pointer1.get_next()

    while pointer1 and pointer2:
        if pointer1 == pointer2:
            return pointer2.data

        pointer1 = pointer1.get_next()
        pointer2 = pointer2.get_next()

    return None
