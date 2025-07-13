# Node class definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to reverse the linked list
def reverseLinkedList(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev  # new head of reversed list

# Utility function to build a linked list from a list of integers
def buildLinkedList(arr):
    if not arr or arr[0] == -1:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        if value == -1:
            break
        current.next = Node(value)
        current = current.next
    return head

# Utility function to print a linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print(-1)

# Main function to read input and run test cases
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        arr = list(map(int, input().split()))
        head = buildLinkedList(arr)
        reversed_head = reverseLinkedList(head)
        printLinkedList(reversed_head)
