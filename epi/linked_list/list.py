class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def search_list(L, key):
        while L and L.data!=key:
            L = L.next
        return L

    def insert_after(node, new_node):
        new_node.next = node.next
        node.next = new_node

    def delete_after(node):
        node.next = node.next.next

    def merge_two_sorted_lists(L1, L2):
        dummy_head = tail = ListNode()

        while L1 and L2:
            if L1.data <= L2.data:
                tail.next = L1
                L1 = L1.next
            else:
                tail.next = L2
                L2 = L2.next
            tail = tail.next

        tail.next = L1 or L2
        return
