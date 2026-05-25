class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        self.head = _merge_sort(self.head)



def _merge_sort(head):
    if head is None or head.next is None:
        return head
    mid = _get_middle(head)
    second_half = mid.next
    mid.next = None
    left = _merge_sort(head)
    right = _merge_sort(second_half)
    return _merge(left, right)


def _get_middle(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def _merge(l1, l2):
    dummy = Node(0)
    current = dummy
    while l1 and l2:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 if l1 else l2
    return dummy.next


def merge_two_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    merged_head = _merge(list1.head, list2.head)
    result = LinkedList()
    result.head = merged_head
    return result


if __name__ == "__main__":
    # Реверс
    ll = LinkedList()
    for x in [3, 1, 4, 1, 5, 9, 2, 6]:
        ll.append(x)
    print("Original :", ll.to_list())
    ll.reverse()
    print("Reversed :", ll.to_list())

    # Сортування
    ll2 = LinkedList()
    for x in [5, 3, 8, 1, 7]:
        ll2.append(x)
    print("\nПеред сортуванням:", ll2.to_list())
    ll2.sort()
    print("Після сортування :", ll2.to_list())

    a = LinkedList()
    b = LinkedList()
    for x in [1, 3, 5]:
        a.append(x)
    for x in [2, 4, 6]:
        b.append(x)
    merged = merge_two_sorted_lists(a, b)
    print("\nMerge [1,3,5] + [2,4,6]:", merged.to_list())