"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

# q for bfs
#stack for dfs

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
            raise IndexError('vertex does not exist')


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()
        q.enqueue(starting_vertex)

        while q.size() > 0:
            #take the first item off stack
            v = q.dequeue()

            # add it to the visited set
            if v not in visited:

                visited.add(v)


                print(v)

                #get its neighbors and add them to the stack
                for x in self.get_neighbors(v):
                    q.enqueue(x)
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        visited = set()
        s.push(starting_vertex)

        while s.size() > 0:

            v = s.pop()

            if v not in visited:

                print(v)
                visited.add(v)

                for x in self.get_neighbors(v):
                    s.push(x)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        print(starting_vertex)

        if visited is None:
            visited = set()

        visited.add(starting_vertex)

        for child_vert in self.get_neighbors(starting_vertex):
            if child_vert not in visited:
                self.dft_recursive(child_vert,visited)
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        visited = set()
        q.enqueue([starting_vertex])

        while q.size()>0:
            path = q.dequeue()

            current = path[-1]

            if current== destination_vertex:
                return path

            else:
                if current not in visited:
                    visited.add(current)

                    for vertex in self.get_neighbors(current):
                        if vertex not in visited:

                            new_path = path.copy()

                            new_path.append(vertex)

                            q.enqueue(new_path)
        return None

        
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()
        s.push([starting_vertex])

        while s.size()>0:
            path = s.pop()

            current = path[-1]

            if current == destination_vertex:
                return path

            else:
                if current not in visited:
                    visited.add(current)

                    for vertex in self.get_neighbors(current):
                        if vertex not in visited:

                            new_path = path.copy()
                            new_path.append(vertex)

                            s.push(new_path)

        return None

    def dfs_recursive(self, start_vert, target_value, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        print(start_vert)

        if visited is None:
            visited = set()

        if path is None:
            path = []

        visited.add(start_vert)

        path = path + [start_vert]

        #base case
        if start_vert == target_value:
            return path

        for child_vert in self.vertices[start_vert]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(child_vert, target_value,visited, path)

                if new_path:
                    return new_path

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
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
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
