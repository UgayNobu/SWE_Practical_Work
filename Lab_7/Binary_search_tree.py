## Step 1: Define the Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

## Step 2: Implement the Binary Search Tree Class with all Methods
class SearchTree:
    def __init__(self):
        self.root = None

    ## Step 3: Implement the Insertion Method
    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._add_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._add_recursive(current.right, value)

    ## Step 4: Implement the Search Method
    def find(self, value):
        return self._find_recursive(self.root, value)

    def _find_recursive(self, current, value):
        if current is None or current.value == value:
            return current
        if value < current.value:
            return self._find_recursive(current.left, value)
        return self._find_recursive(current.right, value)

    ## Step 5: Implement Traversal Methods
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current, result):
        if current:
            self._inorder_recursive(current.left, result)
            result.append(current.value)
            self._inorder_recursive(current.right, result)

    def preorder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, current, result):
        if current:
            result.append(current.value)
            self._preorder_recursive(current.left, result)
            self._preorder_recursive(current.right, result)

    def postorder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, current, result):
        if current:
            self._postorder_recursive(current.left, result)
            self._postorder_recursive(current.right, result)
            result.append(current.value)

    ## Step 6: Implement the Deletion Method
    def remove(self, value):
        self.root = self._remove_recursive(self.root, value)

    def _remove_recursive(self, current, value):
        if current is None:
            return current
        if value < current.value:
            current.left = self._remove_recursive(current.left, value)
        elif value > current.value:
            current.right = self._remove_recursive(current.right, value)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            current.value = self._min_value(current.right)
            current.right = self._remove_recursive(current.right, current.value)
        return current

    def _min_value(self, current):
        while current.left is not None:
            current = current.left
        return current.value

    ## Exercise Methods

    # Find maximum value
    def max_value(self):
        return self._recursive_max(self.root)

    def _recursive_max(self, current):
        if current is None:
            return None
        if current.right is None:
            return current.value
        return self._recursive_max(current.right)

    # Count total nodes
    def total_nodes(self):
        if self.root is None:
            return 0
        count = 0
        stack = [self.root]
        while stack:
            current = stack.pop()
            count += 1
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return count

    # Level-order traversal
    def level_order(self):
        result = []
        max_depth = self.height()
        for depth in range(max_depth + 1):
            self._level_traverse(self.root, depth, result)
        return result

    def _level_traverse(self, current, depth, result):
        if current is None:
            return
        if depth == 0:
            result.append(current.value)
        else:
            self._level_traverse(current.left, depth - 1, result)
            self._level_traverse(current.right, depth - 1, result)

    # Find the height of the BST
    def height(self):
        if not self.root:
            return -1
        h = -1
        queue = [self.root]
        while queue:
            nodes_at_level = len(queue)
            h += 1
            for _ in range(nodes_at_level):
                current = queue.pop(0)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return h

# Testing the SearchTree class with the implemented methods
tree = SearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    tree.add(value)

print("In-order traversal:", tree.inorder())
print("Pre-order traversal:", tree.preorder())
print("Post-order traversal:", tree.postorder())

print("Find 4:", tree.find(4))
print("Find 9:", tree.find(9))

tree.remove(3)
print("In-order after removing 3:", tree.inorder())

print("Maximum value:", tree.max_value())
print("Total number of nodes:", tree.total_nodes())
print("Level-order traversal:", tree.level_order())
print("Height of the BST:", tree.height())
