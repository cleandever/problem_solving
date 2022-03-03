class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        # move step one
        slow = slow.next
        # move step two
        fast = fast.next.next

        # they met
        if slow == fast:
            return True
    return False


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)

    # node1 -> node2 -> node3 -> node4 -> node5 -> node6 -> node3 -> ...
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    # cycle
    node6.next = node3

    head = node1
    assert has_cycle(head)

