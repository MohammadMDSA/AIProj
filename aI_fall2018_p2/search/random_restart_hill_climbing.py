import random
import types

from aI_fall2018_p1.search.p1_search import Search
from aI_fall2018_p2.search.hill_climbing import HillClimbing


class RandomRestartHillClimbing(HillClimbing):
    random_number = 0
    MAX_RANDOM = 10

    def __init__(self, graph=None, objective_func=types.FunctionType):
        super().__init__(graph, objective_func)

    def search(self, start, goal):
        self.random_number = 0
        super().search(start, goal)

    def get_next_state(self, state):
        current_objective = self.objectiveFunction(state)
        next_state = None
        next_max_objective = -1.0
        for child, _ in self.graph[state]:
            child_objective = self.objectiveFunction(child)
            if child_objective > next_max_objective:
                next_max_objective = child_objective
                next_state = child

        if next_state is not None and next_max_objective <= current_objective:
            if self.random_number < self.MAX_RANDOM:
                self.random_number += 1
                return random.choice(self.graph.keys())
            return None
        return next_state
