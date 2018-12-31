from queue import Queue, PriorityQueue

from p1_search import Search


class UCSSearch(Search):

    def __init__(self, graph=None):
        super().__init__(graph)

    def search(self, start, goal):
        frontier = PriorityQueue()
        frontier.put((0, start))  # (priority, node)
        explored = []

        parent = {}

        while True:
            if frontier.empty():
                raise Exception("No way Exception")

            ucs_w, current_node = frontier.get()
            explored.append(current_node)

            if current_node == goal:
                break

            for node, cost in self.graph[current_node]:
                if node not in explored:
                    parent[node] = current_node
                    frontier.put((ucs_w + cost, node))

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

g = UCSSearch(graph=tree)
print(g.search('A', 'Y'))
