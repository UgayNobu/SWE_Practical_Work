## Step 1: Implement the Graph Class

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

# Test the Graph class
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()

## Step 2: Implement Depth-First Search (DFS)

class Graph:
    # ... (previous methods remain the same)

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)
    
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

# Test DFS
print("\nDFS starting from vertex 0:")
g.dfs(0)

## Step 3: Implement Breadth-First Search (BFS)

from collections import deque

class Graph:
    # ... (previous methods remain the same)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Test BFS
print("\nBFS starting from vertex 0:")
g.bfs(0)

## Step 4: Implement a Method to Find All Paths

class Graph:
    # ... (previous methods remain the same)

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph:
            return []
        paths = []
        for neighbor in self.graph[start_vertex]:
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, end_vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

# Test finding all paths
print("\nAll paths from vertex 0 to vertex 3:")
all_paths = g.find_all_paths(0, 3)
for path in all_paths:
    print(' -> '.join(map(str, path)))

## Step 5: Implement a Method to Check if the Graph is Connected

class Graph:
    # ... (previous methods remain the same)

    def is_connected(self):
        if not self.graph:
            return True
        start_vertex = next(iter(self.graph))
        visited = set()
        self._dfs_recursive(start_vertex, visited)
        return len(visited) == len(self.graph)

# Test if the graph is connected
print("\nIs the graph connected?", g.is_connected())

# Add a disconnected vertex and test again
g.add_vertex(4)
print("After adding a disconnected vertex:")
print("Is the graph connected?", g.is_connected())


### Exercises for Students

## Implement a method to find the shortest path between two vertices using BFS.

def in_place_quick_sort(data, start=0, end=None):
    if end is None:
        end = len(data) - 1
    
    if start < end:
        pivot_pos = partition(data, start, end)
        in_place_quick_sort(data, start, pivot_pos - 1)
        in_place_quick_sort(data, pivot_pos + 1, end)
    
    return data

def partition(data, left, right):
    pivot_element = data[right]
    left_marker = left - 1
    
    for current_index in range(left, right):
        if data[current_index] <= pivot_element:
            left_marker += 1
            data[left_marker], data[current_index] = data[current_index], data[left_marker]
    
    data[left_marker + 1], data[right] = data[right], data[left_marker + 1]
    return left_marker + 1

# Test in-place Quick Sort with unique variable names
test_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = in_place_quick_sort(test_list.copy())
print("In-Place Quick Sort Result:", sorted_list)

## Add a method to detect cycles in the graph.

def optimized_bubble_sort(sequence):
    length = len(sequence)
    for pass_num in range(length):
        has_swapped = False
        for index in range(0, length - pass_num - 1):
            if sequence[index] > sequence[index + 1]:
                sequence[index], sequence[index + 1] = sequence[index + 1], sequence[index]
                has_swapped = True
        if not has_swapped:
            break
    return sequence

# Test optimized Bubble Sort with unique variable names
test_sequence = [64, 34, 25, 12, 22, 11, 90]
sorted_sequence = optimized_bubble_sort(test_sequence.copy())
print("Optimized Bubble Sort Result:", sorted_sequence)

## Create a method to determine if the graph is bipartite.

def visualize_bubble_sort(data):
    num_elements = len(data)
    
    def print_data(data, highlight=None):
        # Print the data with simple visualization by highlighting swapped elements
        print(" ".join(
            f"[{val}]" if index == highlight else str(val) 
            for index, val in enumerate(data)
        ))

    def bubble_sort_with_visualization(data):
        for pass_index in range(num_elements):
            sorted_flag = False
            for i in range(0, num_elements - pass_index - 1):
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]
                    sorted_flag = True
                    print_data(data, highlight=i+1)  # Highlight the recently swapped element
            if not sorted_flag:
                break

    print("Starting Bubble Sort Visualization:")
    print_data(data)  # Initial state
    bubble_sort_with_visualization(data)
    print("Final Sorted List:")
    print_data(data)

# Test visualization with Bubble Sort
sample_data = [64, 34, 25, 12, 22, 11, 90]
visualize_bubble_sort(sample_data)
