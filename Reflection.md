### (a) Documentation

## Main Concepts Applied

In this project, I implemented various key concepts in graph theory using Python. The graph is one of the most versatile and widely-used data structures, and I applied it in the context of creating a graph class that supports common graph operations. Below are the key concepts and functionalities I implemented:

# Graph Class:

I created a Graph class to represent an undirected graph. In this class, each vertex is represented as a key in a dictionary, and its edges (or neighbors) are stored as a list of vertices.
Add Vertex: This method allows the addition of a vertex to the graph, ensuring that it only adds a new vertex if it does not already exists in the graph. This ensures that vertices are unique within the graph.
Add Edge: The add_edge method is used to connect two vertices by adding each vertex to the other's list of neighbors. This method works for undirected graphs because edges are bidirectional. The function automatically adds the vertices if they don't exists, which helps avoid errors when adding edges.
Depth-First Search (DFS):

DFS is a graph traversal algorithm that explores a graph by starting from a given node and exploring as far down a branch as possible before backtracking.
In this implementation, I used recursion to traverse the graph. The function starts at a given vertex and visits its neighbors, marking them as visited. The algorithm recursively visits each unvisited neighbor.
Visited Set: I used a visited set to ensure that each vertex is only visited once, avoiding cycles and infinite loops in the graph.
Breadth-First Search (BFS):

BFS explores the graph level by level, visiting all the neighbors of a vertex before moving on to the next level. I used a queue to implement this algorithm. A queue is ideal for BFS because it processes vertices in the order they are discovered (FIFO – First In, First Out).
The function starts by enqueuing the starting vertex and exploring all its unvisited neighbors before dequeuing the first vertex and moving on to its neighbors.
Finding All Paths:

This method finds all possible paths from a starting vertex to a destination vertex. The method recursively explores all neighbors of a vertex, ensuring it does not revisit a vertex already in the current path.
The main idea was to build each path progressively as the algorithm traverses the graph, and when the destination is reached, the current path is added to the list of all paths.
Graph Connectivity:

A graph is connected if there is a path between any two vertices in the graph. I implemented a method to check if a graph is connected by performing a DFS starting from any arbitrary vertex. If the number of visited vertices equals the total number of vertices in the graph, the graph is connected; otherwise, it is not.
This method ensures that the graph is properly connected and helps identify disconnected components if any exist.

## New Skills or Knowledge Acquired

# Graph Representation:

I gained a deeper understanding of how to represent a graph using an adjacency list. The adjacency list representation is efficient in terms of space and easy to implement in Python using dictionaries and lists.
I also learned the practical applications of this representation in real-world problems, such as social networks, web page linking, and network routing.

# Graph Traversal Algorithms:

I deepened my understanding of graph traversal algorithms like DFS and BFS. Both of these algorithms are widely used in search problems, and I learned how to implement them efficiently.
Through DFS, I learned how to manage recursion, which is often tricky with graph problems because it requires careful tracking of visited nodes to avoid cycles.

BFS, on the other hand, gave me a better understanding of how to explore graphs in layers, which is crucial in finding the shortest path between vertices in an unweighted graph.
Recursive Programming:

Implementing DFS and pathfinding taught me a lot about recursive programming. Initially, I was not very confident in using recursion to solve graph problems, but after completing this project, I am much more comfortable applying recursion in problems like graph traversal and pathfinding.

I also learned how recursion can be an elegant solution to exploring all paths in a graph or managing states during a search.
Problem Solving:

This project challenged me to think critically about how to break down complex problems like pathfinding and connectivity into smaller, manageable tasks. By systematically tackling each task (graph construction, DFS/BFS traversal, pathfinding), I learned how to approach graph problems logically and sequentially.

### (b) Reflection

## What I Learned

This project has greatly enhanced my knowledge of graph theory and has given me valuable hands-on experience in implementing key algorithms like DFS, BFS, and pathfinding. I learned how to design and implement a graph structure, perform graph traversal, and find all possible paths between two vertices.

Before this project, I had only theoretical knowledge of graph traversal algorithms, but now I understand their implementation and real-world applications much better. For example, BFS is useful in finding the shortest path in unweighted graphs, and DFS is great for exhaustive searches.

In addition, the recursive nature of DFS and pathfinding has helped me develop a more thorough understanding of recursion as a programming technique. I can now apply recursion confidently to other problems as well.

One of the key takeaways was the importance of edge cases in graph algorithms. For example, handling disconnected graphs in the connectivity check or ensuring that cycles are avoided in DFS required careful attention to detail.

## Challenges Faced and How I Overcame Them

# Cycle Detection in DFS:

Initially, I faced a challenge when working with DFS because the algorithm could run into infinite loops if it revisited a node. For example, if there was a cycle in the graph, DFS would get stuck in a loop.
I overcame this by maintaining a visited set that tracks nodes already explored. This prevented the DFS from revisiting nodes and helped ensure that each node was processed only once.

# Pathfinding with Recursion:

Finding all paths between two nodes was tricky because I had to manage multiple recursive calls and ensure that each path was correctly built. Initially, the function was returning incomplete or incorrect paths.
To resolve this, I carefully ensured that paths were passed along recursively and that nodes were not revisited in the current path. Testing the function with simple graphs helped identify issues in the recursive logic.

# Graph Connectivity Check:

Ensuring the graph connectivity check was working correctly proved challenging, especially after adding disconnected vertices. The first version of the check failed to properly detect when a graph was not fully connected.
I fixed this by ensuring that after performing DFS from an arbitrary starting vertex, the number of vertices visited matched the total number of vertices in the graph. If they didn’t match, it indicated that the graph was disconnected.

# Edge Cases:

Handling edge cases such as graphs with no vertices, graphs with a single vertex, or graphs with disconnected components required careful thought.
I wrote additional test cases to check for these edge cases and ensured my methods handled them gracefully. For instance, I made sure that is_connected returned True for empty graphs and single-vertex graphs.
