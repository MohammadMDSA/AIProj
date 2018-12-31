from p1_search import Search
from queue import PriorityQueue


class AStarSearch(Search):

    def __init__(self, heuristic, graph=None):
        super().__init__(graph)
        self.heuristic = heuristic

    def search(self, start, goal):
        parent = {}
        frontier = PriorityQueue()
        frontier.put((0, start))
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for next, cost in self.graph[current]:
                new_cost = cost_so_far[current] + cost
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic[next]
                    parent[next] = current
                    frontier.put((priority, next))
                    came_from[next] = current

        result = []
        current = goal
        result.append(goal)
        while not current == start:
            current = parent[current]

            result.append(current)

        result.reverse()
        return result
