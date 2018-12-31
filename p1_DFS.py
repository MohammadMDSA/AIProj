from p1_search import Search


class DFSSearch(Search):
    limitation = -1
    iterative = False

    def __init__(self, iterative=False, limitation=-1, graph=None):
        super().__init__(graph)
        self.limitation = limitation
        self.iterative = iterative

    def search(self, start, goal):
        if self.iterative:
            return self.iterative_dfs(start, goal)

        if self.limitation == -1:
            return self.normal_dfs(start, goal)
        else:
            return self.limited_dfs(start, goal, self.limitation)

    def iterative_dfs(self, start, goal):
        parent = {}

        def dls(node, depth):
            if depth is 0:
                if node is goal:
                    return node, True
                else:
                    return None, True
            elif depth > 0:
                any_remaining = False
                for child, _ in self.graph[node]:
                    parent[child] = node
                    found, remaining = dls(child, depth - 1)
                    if found is not None:
                        return found, True
                    if remaining:
                        any_remaining = True
                return None, any_remaining

        for depth in range(self.graph.__len__() + 1):
            found, remaining = dls(start, depth)
            if found is not None:
                break

        if found is None:
            return None

        result = []
        current = goal
        result.append(goal)
        while not current == start:
            current = parent[current]

            result.append(current)

        result.reverse()
        return result

    def limited_dfs(self, start, goal, limit):

        parent = {}

        def _walk(nodee, limit):
            if limit <= -1:
                return
            for v, _ in self.graph[nodee]:
                if v not in parent:
                    parent[v] = nodee
                    if node is goal:
                        return
                    _walk(v, limit - 1)

        for node in self.graph:
            if node not in parent:
                parent[node] = None
                _walk(node, limit)

        result = []
        current = goal
        result.append(goal)
        while not current == start:
            current = parent[current]

            result.append(current)

        result.reverse()
        return result

    def normal_dfs(self, start, goal):
        parent = {}

        def _walk(nodee):
            for v, _ in self.graph[nodee]:
                if v not in parent:
                    parent[v] = nodee
                    if node is goal:
                        return
                    _walk(v)

        for node in self.graph:
            if node not in parent:
                parent[node] = None
                _walk(node)

        result = []
        current = goal
        result.append(goal)
        while not current == start:
            current = parent[current]

            result.append(current)

        result.reverse()
        return result


tree = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['A', 'F', 'G', 'H'],
    'C': ['A', 'H'],
    'D': ['A', 'I', 'J'],
    'E': ['A', 'K', 'L'],
    'F': ['B', 'G', 'M', 'N', 'O'],
    'G': ['B', 'F', 'P', 'Q', 'R'],
    'H': ['C', 'G', 'S'],
    'I': ['D'],
    'J': ['D', 'T', 'U'],
    'K': ['E'],
    'L': ['E', 'V'],
    'M': ['F'],
    'N': ['F'],
    'O': ['F'],
    'P': ['G'],
    'Q': ['G'],
    'R': ['G'],
    'S': ['H', 'W', 'X'],
    'T': ['J'],
    'U': ['J', 'Y', 'Z'],
    'V': ['L'],
    'W': ['S'],
    'X': ['S'],
    'Y': ['U'],
    'Z': ['U']
}

g = DFSSearch(graph=tree)
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 0)
# g.add_edge(2, 3)
# g.add_edge(1, 4)
# g.add_edge(4, 5)
# g.add_edge(3, 5)

print(g.search('A', 'Y'))
