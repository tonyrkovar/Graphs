"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print('Error: Vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print("Error: Vertex doesn't exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a queue
        q = Queue()
        # enqueue the starting vertex
        q.enqueue(starting_vertex)
        # Create a set to store our visited verticies
        visited = set()
        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # Check if it has been visited
            if v not in visited:
                print(v)
                visited.add(v)
            # if not visited
                # Mark as visited
                # Enqueue all adjacent veticies
                # loop
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack
        s = Stack()
        # pust the starting vertex into the stack
        s.push(starting_vertex)
        # Create a set to store our visited verticies
        visited = set()
        # While the stack is not empty
        while s.size() > 0:
            # pop the first vertex from the stack
            v = s.pop()
        # Check if it has been visited
            if v not in visited:

                # if not visited mark as visited
                print(v)
                visited.add(v)
                # push all adjacent veticies into the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)
        # loop

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)
        else:
            return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        -- This will be very similar to bft, the only
        difference is that you will only return
        the parth you took to get to a certain
        vertex --
        """
        # Breadth first uses a queue
        q = Queue()
        # When you initialize the code you want to enqueue your starting vertex
        q.enqueue(starting_vertex)
        # You also want to track the vertecies you interact with along the way(This is what you will return)
        visited = []
        # Run your logic until you visit the target node
        while destination_vertex not in visited:
            # Take the next value out of your queue
            v = q.dequeue()
            # If you haven't visited the value yet
            if v not in visited:
                # Append the value to visited
                visited.append(v)
                # Get the neighboring Verticies values
                for neighbor in self.get_neighbors(v):
                    # Check ahead by one vertex for the destination
                    for next_neighbor in self.get_neighbors(neighbor):
                        # If our node one ahead is the destination, return the value
                        if next_neighbor == destination_vertex:
                            visited.append(neighbor)
                            visited.append(next_neighbor)
                            # Return visited, exit code
                            return visited
                    # Enqueue if the target value isn't two values ahead, traverse
                    q.enqueue(neighbor)

        return visited

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = []
        while destination_vertex not in visited:
            vert = s.pop()
            if vert not in visited:
                visited.append(vert)
                for neighbor in self.get_neighbors(vert):
                    if neighbor == destination_vertex:
                        visited.append(neighbor)
                    s.push(neighbor)
        return visited

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = []

        if starting_vertex not in visited:
            if starting_vertex == destination_vertex:
                visited.append(starting_vertex)
                print(visited)
                return visited
            visited.append(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                if neighbor == destination_vertex:
                    visited.append(neighbor)
                    print(visited)
                    return visited
                print(neighbor, visited)
                self.dfs_recursive(neighbor, destination_vertex, visited)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
