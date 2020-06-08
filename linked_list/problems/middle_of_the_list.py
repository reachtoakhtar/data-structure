from linked_list.exception import EmptyListError

__author__ = "akhtar"


def find_middle_of_the_list(linked_list):
    """
    Find the middle node of a single linked list.

    :param SingleLinkedList linked_list: The linked list to operate.
    :return: data for middle node of the list.
    :rtype: int
    :raises EmptyListError: if the list is empty.
    """
    if linked_list.head is None:
        raise EmptyListError("List is empty, cannot find middle")

    pointer1 = linked_list.head
    pointer2 = linked_list.head
    count = 0

    # Move one pointer at one step, second pointer at two steps.
    # The pointer which traversed at one step a time would point to
    # middle node at the end of the iteration.
    while pointer1.get_next():
        if count == 0:
            pointer1 = pointer1.get_next()
            count = 1

        elif count == 1:
            pointer1 = pointer1.get_next()
            pointer2 = pointer2.get_next()
            count = 0

    return pointer2.data
