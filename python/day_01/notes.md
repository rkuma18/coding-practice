# 🧹 Remove Elements from a Singly Linked List in Python

This project demonstrates how to implement a **singly linked list** and remove **all nodes** containing a specific value using a **standalone function** in Python. It includes helper functions to build and print the linked list for testing and demonstration purposes.

---

## 📌 Problem Statement

Given the head of a singly linked list and an integer value `target`, remove **all nodes** in the list that contain `target` and return the updated list.

### Example:

| Input List         | Target | Output List       |
|--------------------|--------|-------------------|
| 1 → 2 → 3 → None    | 3      | 1 → 2 → None      |
| 8 → 1 → 1 → 4 → 12 | 1      | 8 → 4 → 12 → None |
| 7 → 12 → 2 → 9     | 7      | 12 → 2 → 9 → None |

---

## 🧠 Approach

- A **dummy node** is used to simplify deletion logic, especially for head deletions.
- The list is traversed using a `current` pointer.
- When a node's value equals the `target`, it is removed by updating the `next` reference of the previous node.

---

## 🛠 Functions

### `remove_elements(head, target)`
Removes all nodes from the linked list starting at `head` that contain the value `target`.

### `build_linked_list(values)`
Helper function to build a linked list from a Python list.

### `print_linked_list(head)`
Helper function to print the linked list in a readable format.

---

## 🚀 How to Use

```python
# Build the linked list
head = build_linked_list([1, 2, 3])

# Remove target value
new_head = remove_elements(head, 3)

# Print the result
print_linked_list(new_head)  # Output: 1 -> 2 -> None
