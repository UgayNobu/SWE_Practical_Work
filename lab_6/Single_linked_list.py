## Step 1: Define the Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

## Step 2: Create the LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None

## Step 3: Implement the Append Method
class LinkedList:
    # ... (previous code)

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# Test the append method
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

## Step 4: Implement the Display Method
class LinkedList:
    # ... (previous code)

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

# Test the display method
ll.display()  # Output: 1 -> 2 -> 3

## Step 5: Implement the Insert Method
class LinkedList:
    # ... (previous code)

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

# Test the insert method
ll.insert(4, 1)
ll.display()  # Output: 1 -> 4 -> 2 -> 3

## Step 6: Implement the Delete Method
class LinkedList:
    # ... (previous code)

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

# Test the delete method
ll.delete(2)
ll.display()  # Output: 1 -> 4 -> 3 

## Step 7: Implement the Search Method
class LinkedList:
    # ... (previous code)

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

# Test the search method
print(ll.search(4))  # Output: 1
print(ll.search(5))  # Output: -1

## Step 8: Implement the Reverse Method
class LinkedList:
    # ... (previous code)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Test the reverse method
ll.reverse()
ll.display()  # Output: 3 -> 4 -> 1
 

           ### Exercises for Students

## Implement a method to find the middle element of the linked list.
class LinkedList:
    # Previous methods...

    # Exercise: Find the middle element of the linked list
    def find_middle(self):
        mid_ptr = self.head
        end_ptr = self.head
        while end_ptr and end_ptr.next:
            mid_ptr = mid_ptr.next
            end_ptr = end_ptr.next.next
        return mid_ptr.data if mid_ptr else None

# Example usage for finding the middle element
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
print("Middle element:", ll.find_middle())  # Expected output: 3

## Create a method to detect if the linked list has a cycle.
class LinkedList:
    # Previous methods...

    # Exercise: Detect if the linked list has a cycle
    def has_cycle(self):
        walker = self.head
        runner = self.head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        return False

# Example usage for cycle detection
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
print("Has cycle:", ll.has_cycle())  # Expected output: False

# Creating a cycle for testing
node = ll.head
while node.next:  # Go to last node
    node = node.next
node.next = ll.head  # Create cycle
print("Has cycle:", ll.has_cycle())  # Expected output: True

## Implement a method to remove duplicates from an unsorted linked list.
class LinkedList:
    # Previous methods...

    # Exercise: Remove duplicates from an unsorted linked list
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

# Example usage for removing duplicates
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(3)
ll.append(3)
ll.display()  # Output before removing duplicates: 1 -> 2 -> 2 -> 3 -> 3
ll.remove_duplicates()
ll.display()  # Expected output after removing duplicates: 1 -> 2 -> 3

