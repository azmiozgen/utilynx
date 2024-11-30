#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def has_cycle(head):
    """
    Check if a linked list has a cycle.
    Time complexity: O(n)
    Space complexity: O(1)
    """
    if not head:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False


def merge_two_sorted_linked_lists(list1, list2):
    """
    list1 and list2 are the heads of two sorted linked lists.
    Merge the two lists into one sorted list.
    Return the head of the merged linked list.

    """
    dummy = ListNode()
    cur = dummy

    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next

    if list1:
        cur.next = list1
    else:
        cur.next = list2

    return dummy.next


if __name__ == '__main__':
    ## Test has_cycle
    print()
    print('Test has_cycle with a linked list with cycle (3 -> 2 -> 0 -> 2)')
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = head.next
    print(has_cycle(head))

    ## Test merge_two_sorted_linked_lists
    print()
    print('Test merge_two_sorted_linked_lists with two linked lists'
          '(1 -> 2 -> 4) and (1 -> 3 -> 4)')
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    merged = merge_two_sorted_linked_lists(list1, list2)
    while merged:
        print(merged.val, end='->')
        merged = merged.next
