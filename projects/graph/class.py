
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



g = Graph()

g.add_vertex(99)
g.add_vertex(3)
g.add_vertex(3490)

g.add_edge(99,3490)
g.add_edge(99,3)
g.add_edge(3,99)

print(g.vertices)

