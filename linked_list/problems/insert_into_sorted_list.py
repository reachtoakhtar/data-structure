from linked_list.exception import EmptyListError

__author__ = "akhtar"


def insert_into_sorted_list(linked_list, data):
    """
    Insert a node in a sorted linked list at its proper position.

    :param SingleLinkedList linked_list: The linked list to operate.
    :return: nothing.
    :rtype: None
    :raises EmptyListError: if the list is empty.
    """
    if linked_list.head is None:
        raise EmptyListError("List is empty, cannot insert")

    position = 1
    pointer = linked_list.head
    insert_at_end = True
    while pointer:
        if pointer.data >= data:
            linked_list.insert_at_position(position, data)
            insert_at_end = False
            break
        pointer = pointer.get_next()
        position += 1

    if insert_at_end:
        linked_list.insert_at_end(data)
