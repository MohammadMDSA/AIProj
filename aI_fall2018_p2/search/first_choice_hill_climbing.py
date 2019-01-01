import random
import types

from aI_fall2018_p2.search.hill_climbing import HillClimbing


class FirstChoiceHillClimbing(HillClimbing):

    MAX_RANDOM = 10

    def __init__(self, graph=None, objective_func = types.FunctionType):
        super().__init__(graph, objective_func)

    def get_next_state(self, state):
        current_objective = self.objectiveFunction(state)
        for i in range(self.MAX_RANDOM):
            random_neighbour = random.choice(self.graph.keys())
            if self.objectiveFunction(random_neighbour) > current_objective:
                return random_neighbour
        return None
