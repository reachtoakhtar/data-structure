from linked_list.exception import EmptyListError

__author__ = "akhtar"


def loop_in_a_list(linked_list):
    """
    Check whether a given linked list ends in a cycle (cyclic). If yes,
    find the start node of the loop.

    :param SingleLinkedList linked_list: The linked list to operate.
    :return: whether cyclic, and also start node if it is cyclic.
    :rtype: tuple
    :raises EmptyListError: if the list is empty.
    """
    if linked_list.head is None:
        raise EmptyListError("List is empty, cannot continue operation")

    is_cyclic = False
    slow_ptr = linked_list.head
    fast_ptr = linked_list.head

    # fast_ptr traverses two steps at a time, slow_ptr traverses one step at
    # a time. If they meet at a point, there is a loop in the list.
    while slow_ptr and fast_ptr and fast_ptr.get_next():
        slow_ptr = slow_ptr.get_next()
        fast_ptr = fast_ptr.get_next().get_next()
        if fast_ptr == slow_ptr:
            is_cyclic = True
            break

    if is_cyclic:
        # Set slow_ptr to head node
        slow_ptr = linked_list.head

        # Now, traverse both pointers one step a time, the point where they meet
        # is the beginning of the loop.
        while slow_ptr != fast_ptr:
            fast_ptr = fast_ptr.get_next()
            slow_ptr = slow_ptr.get_next()

    return is_cyclic, fast_ptr and fast_ptr.data


def lenth_of_the_loop(linked_list):
    """
    Find the length of the loop in a linked list if it exists.

    :param SingleLinkedList linked_list: The linked list to operate.
    :return: the count of number of nodes in the loop.
    :rtype: int
    :raises EmptyListError: if the list is empty.
    """
    if linked_list.head is None:
        raise EmptyListError("List is empty, cannot continue operation")

    is_cyclic = False
    slow_ptr = linked_list.head
    fast_ptr = linked_list.head

    # fast_ptr traverses two steps at a time, slow_ptr traverses one step at
    # a time. If they meet at a point, there is a loop in the list.
    while slow_ptr and fast_ptr and fast_ptr.get_next():
        slow_ptr = slow_ptr.get_next()
        fast_ptr = fast_ptr.get_next().get_next()
        if fast_ptr == slow_ptr:
            is_cyclic = True
            break

    counter = 0
    if is_cyclic:
        # At this point, fast_ptr == slow_ptr.
        # Keep moving the fast_ptr till it comes back again to slow_ptr,
        # increasing the counter at each iteration.
        counter += 1
        while slow_ptr != fast_ptr.get_next():
            fast_ptr = fast_ptr.get_next()
            counter += 1

    return counter
