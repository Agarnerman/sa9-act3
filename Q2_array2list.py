class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next, prev as None

    def __str__(self):
        return f'{self.data} -> {self.next}'

# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        temp = self.head
        while temp:
            print(f'{temp.data} -> ', end="")
            temp = temp.next
        print('None')

    def __str__(self):
        return f' {self.printList()}'

    def __iter__(self):  # so you can do the for loop iteration..
        node = self.head
        while node is not None:
            yield node
            node = node.next

# Function to convert an array to a linked list
def arrayToLinkedList(arr):
    # Create an empty linked list
    linked_list = LinkedList()

    # Iterate through the array and insert each element into the linked list
    for item in arr:
        linked_list.head = insert(linked_list.head, item)

    return linked_list

# Function to insert a node at the beginning of the linked list
def insert(root, item):
    # Create a new node
    new_node = Node(item)

    # If the linked list is empty, set the new node as both head and tail
    if root is None:
        root = new_node
        return root

    # Otherwise, set the new node's next pointer to the current head
    new_node.next = root

    # Set the new node as the new head
    root = new_node

    return root

# Create a list of numbers
arr = [10, 12, 11, 11, 11, 12, 11, 10, 13]

# Convert the list to a linked list
linked_list = arrayToLinkedList(arr)

# Print the linked list
print("Linked list:", linked_list)