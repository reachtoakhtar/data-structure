from linked_list.exception import EmptyListError

__author__ = "akhtar"


def reverse_single_linked_list(linked_list):
    """
    Reverse a given single linked list.

    :param SingleLinkedList linked_list: The linked list to operate.
    :return: nothing.
    :rtype: None
    :raises EmptyListError: if the list is empty.
    """
    if linked_list.head is None:
        raise EmptyListError("List is empty, cannot reverse")

    previous = None
    pointer = linked_list.head

    while pointer:
        next = pointer.get_next()
        pointer.set_next(previous)
        previous = pointer
        pointer = next

    linked_list.head = previous
