'''
 # Google
Given a linked list and a value, remove all nodes containing the provided value, and return the resulting list.

Ex: Given the following linked lists and values...

1->2->3->null, value = 3, return 1->2->null
8->1->1->4->12->null, value = 1, return 8->4->12->null
7->12->2->9->null, value = 7, return 12->2->9->null

'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def remove_elements(head, target):
    dummy = Node(0)
    dummy.next = head
    current = dummy

    while current and current.next:
        if current.next.data == target:
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next

def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# Example 1
head1 = build_linked_list([1, 2, 3])
new_head1 = remove_elements(head1, 3)
print_linked_list(new_head1)  # Output: 1 -> 2 -> None

# Example 2
head2 = build_linked_list([8, 1, 1, 4, 12])
new_head2 = remove_elements(head2, 1)
print_linked_list(new_head2)  # Output: 8 -> 4 -> 12 -> None

# Example 3
head3 = build_linked_list([7, 12, 2, 9])
new_head3 = remove_elements(head3, 7)
print_linked_list(new_head3)  # Output: 12 -> 2 -> 9 -> None
