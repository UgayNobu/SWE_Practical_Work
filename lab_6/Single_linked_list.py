## Step 1: Define the Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

## Step 2: Create the LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head to None

    ## Step 3: Implement the Append Method
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    ## Step 4: Implement the Display Method
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    ## Step 5: Implement the Insert Method
    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    ## Step 6: Implement the Delete Method
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    ## Step 7: Implement the Search Method
    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    ## Step 8: Implement the Reverse Method
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    ## Exercise: Find the middle element of the linked list
    def find_middle(self):
        mid_ptr = self.head
        end_ptr = self.head
        while end_ptr and end_ptr.next:
            mid_ptr = mid_ptr.next
            end_ptr = end_ptr.next.next
        return mid_ptr.data if mid_ptr else None

    ## Exercise: Detect if the linked list has a cycle
    def has_cycle(self):
        walker = self.head
        runner = self.head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        return False

    ## Exercise: Remove duplicates from an unsorted linked list
    def remove_duplicates(self):
        node_ptr = self.head
        unique_values = set()
        previous_node = None
        while node_ptr:
            if node_ptr.data in unique_values:
                previous_node.next = node_ptr.next
            else:
                unique_values.add(node_ptr.data)
                previous_node = node_ptr
            node_ptr = node_ptr.next

# Testing the methods
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Original list:")
ll.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5
