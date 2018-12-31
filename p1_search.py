from collections import defaultdict


class Search:
    graph = {}

    def __init__(self, graph = {}):
        if graph is None:
            graph = {}
        else:
            newG = {}
            for key in graph:
                newG[key] = []
                for element in graph[key]:
                    if type(element) == tuple:
                        newG[key].append(element)
                    else:
                        newG[key].append((element, 0))
            graph = newG

        self.graph = graph

    def add_node(self, name):
        if not (name in self.graph):
            self.graph[name] = []
        return self.graph[name]

    def add_edge(self, a, b, a_to_b=0, b_to_a=0):
        if not (a in self.graph):
            self.add_node(a)
        if not (b in self.graph):
            self.add_node(b)

        self.graph[b].append((a, b_to_a))
        self.graph[a].append((b, a_to_b))

    def search(self, start, goal):
        pass


# s = Search();
# s.add_node("a", 2)
# print(s.graph)
# s.add_node("a", 3)
# print(s.graph)
# print(s.graph.__len__())
