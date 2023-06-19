class Graph:
    def __init__(self):
        self.dict = {}

    def addVertex(self, vertex):
        if vertex not in self.dict.keys():
            self.dict[vertex] = []
            return True
        return False

    def BFS(self, vertex):
        queue = [vertex]
        visited = [vertex]

        while queue:
            p = queue.pop(0)
            print(p)
            for adjacentVertex in self.dict[p]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

    def DFS(self, vertex):
        stack = [vertex]
        visited = [vertex]
        while stack:
            p = stack.pop()
            print(p)
            for adjacentVertex in self.dict[p]:
                if adjacentVertex not in visited:
                    stack.append(adjacentVertex)
                    visited.append(adjacentVertex)

    def removeVertex(self, vertex):
        if vertex in self.dict.keys():
            for value in self.dict[vertex]:
                self.dict[value].remove(vertex)
            del self.dict[vertex]
            return True
        return False

    def print_graph(self):
        for vertex in self.dict:
            print(vertex, ":", self.dict[vertex])

    def addEdge(self, vertex1, vertex2):
        if vertex1 and vertex2 in self.dict.keys():
            if vertex2 not in self.dict[vertex1]:
                self.dict[vertex1].append(vertex2)
            if vertex1 not in self.dict[vertex2]:
                self.dict[vertex2].append(vertex1)
            return True
        return False

    def removeEdge(self, vertex1, vertex2):
        if vertex1 and vertex2 in self.dict.keys():
            try:
                self.dict[vertex1].remove(vertex2)
                self.dict[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False


graph = Graph()
graph.addVertex("a")
graph.addVertex("b")
graph.addVertex("c")
graph.addVertex("d")
graph.addVertex("e")
graph.addVertex("f")
graph.addEdge("a", "b")
graph.addEdge("a", "c")
graph.addEdge("b", "d")
graph.addEdge("b", "e")
graph.addEdge("c", "e")
graph.addEdge("d", "e")
graph.addEdge("d", "f")
graph.addEdge("e", "f")


# # graph.removeEdge("a", "c")
# graph.removeVertex("c")
graph.print_graph()
# graph.BFS("a")
graph.DFS("a")
