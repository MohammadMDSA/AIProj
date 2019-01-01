from aI_fall2018_p1.search.p1_search import Search


class BFSSearch(Search):

    def __init__(self, graph=None):
        super().__init__(graph)

    def search(self, start, goal):
        visited = {}

        for key in self.graph:
            visited[key] = False

        queue = [start]

        parent = {start: ''}

        visited[start] = True

        resume = True
        while queue and resume:
            s = queue.pop(0)

            for i,_ in self.graph[s]:
                if not visited[i]:
                    parent[i] = s
                    queue.append(i)
                    visited[i] = True
                    if i is goal:
                        resume = False
                        break;

        result = []
        current = goal
        result.append(goal)
        while not current == start:
            current = parent[current]

            result.append(current)

        result.reverse()
        return result


g = BFSSearch()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.add_edge(1, 4)
g.add_edge(4, 5)
g.add_edge(3, 5)

print(g.search(2, 5))
