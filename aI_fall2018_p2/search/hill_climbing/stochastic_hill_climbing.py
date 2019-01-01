import random
import types

from aI_fall2018_p2.search.hill_climbing.hill_climbing import HillClimbing


class StochasticHillClimbing(HillClimbing):

    def __init__(self, graph=None, objective_func=types.FunctionType):
        super().__init__(graph, objective_func)

    def get_next_state(self, state):
        current_objective = self.objectiveFunction(state)

        better_state = []
        for child,_ in self.graph[state]:
            if self.objectiveFunction(child) > current_objective:
                better_state.append(child)

        if better_state.__len__() is 0:
            return None
        return better_state[random.choice(range(better_state.__len__()))]