
#stacks are for depth first search
#ques are for breadth first search

class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self,vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self,v1,v2):

        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("vertex does not exist")

    def get_neighbors(self,vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):


        pass

    def dft_recursive(self, start_vert, visited = None):

        print(start_vert)

        if visited is None:
            visited = set()

        visited.add(start_vert)

        for child_vert in self.vertices[start_vert]:
            if child_vert not in visited:
                self.dft_recursive(child_vert,visited)

        
    def dfs_recursive(self, start_vert, target_value, visited=None, path=None):
        print(start_vert)

        if visited is None:
            visited = set()

        if path is None:
            path = []

        visited.add(start_vert)

        path = path + [start_vert]

        if start_vert == target_value:
            return path

        for child_vert in self.vertices[start_vert]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(child_vert, target_value, visited, path)

                if new_path:
                    return new_path


g = Graph()

g.add_vertex(99)
g.add_vertex(3)
g.add_vertex(69)
g.add_vertex(79)
g.add_vertex(3490)

g.add_edge(99,3490)
g.add_edge(99,3)
g.add_edge(3,99)
g.add_edge(3,69)
g.add_edge(99, 79)

print(g.vertices)

g.dft_recursive(99)

print(g.dfs_recursive(3,3490))

