### Part 1: Implementing a Stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

# Test the Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Should print 3
print(stack.peek())  # Should print 2
print(stack.size())  # Should print 2

### Part 2: Implementing a Queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

# Test the Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Should print 1
print(queue.front())  # Should print 2
print(queue.size())  # Should print 2

### Part 3: Solving Practical Problems

## Problem 1: Balanced Parentheses
def is_balanced(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

# Test the function
print(is_balanced("((()))"))  # Should print True
print(is_balanced("(()"))  # Should print False

## Problem 2: Reverse a String
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# Test the function
print(reverse_string("Hello, World!"))  # Should print "!dlroW ,olleH"

## Problem 3: Hot Potato Simulation
def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()

# Test the function
names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
print(hot_potato(names, 7))  # The winner's name will be printed

### Exercises for Students
### Implement a function that uses a stack to evaluate postfix expressions.
def evaluate(expression):
    new_stack = []
    for character in expression.split():
        if character.isdigit():
            new_stack.append(int(character))
        else:
            b = new_stack.pop()
            a = new_stack.pop()
            if character == '+':
                new_stack.append(a + b)
            elif character == '-':
                new_stack.append(a - b)
            elif character == '*':
                new_stack.append(a * b)
            elif character == '/':
                new_stack.append(a / b)
    return new_stack.pop()

# Test function
print(evaluate("3 4 + 2 * 7 /"))

### Create a function that uses two stacks to implement a queue
stack_one = []
stack_two = []

# Stack_one function
def stack_one_func(value):
    stack_one.append(value)

# Stack_two function
def stack_two_func():
    if not stack_two:
        while stack_one:
            stack_two.append(stack_one.pop())
    return stack_two.pop() if stack_two else None

# To test the function
stack_one_func(10)
stack_one_func(20)
stack_one_func(30)
print(stack_two_func())
print(stack_two_func())
print(stack_two_func())

### Use a queue to implement a basic task scheduler that processes tasks in the order they were added.
main_queue = []

# Function to add a task to queue
def adding_task(main_task):
    main_queue.append(main_task)

# Function to work the task in order added
def task_processing():
    while main_queue:
        initial_task = main_queue.pop(0)
        print(f"Processing: {initial_task}")

# To test the function
adding_task("Game notification")
adding_task("Phone data storage")
adding_task("Reporting students who failed")
task_processing()

### Implement a function that uses a stack to convert infix expressions to postfix.
def infix_expressions_to_postfix(opperations):
    operators = {'+': 1, '-': 2, '*': 3, '/': 4}
    opperation_stack = []
    output_stack = []

    for sign in opperations:
        if sign.isalnum():
            output_stack.append(sign)
        elif sign == '(':
            opperation_stack.append(sign)
        elif sign == ')':
            while opperation_stack and opperation_stack[-1] != '(':
                output_stack.append(opperation_stack.pop())
            opperation_stack.pop()  # Remove the '(' from the stack
        else:
            while (opperation_stack and opperation_stack[-1] in operators and
                   operators[sign] <= operators[opperation_stack[-1]]):
                output_stack.append(opperation_stack.pop())
            opperation_stack.append(sign)

    while opperation_stack:
        output_stack.append(opperation_stack.pop())

    return ''.join(output_stack)

# Example test for infix to postfix conversion
print(infix_expressions_to_postfix("A + B * C"))  # Should output "A B C * +"
