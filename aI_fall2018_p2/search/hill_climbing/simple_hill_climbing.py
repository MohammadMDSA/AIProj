import types

from aI_fall2018_p2.search.hill_climbing.hill_climbing import HillClimbing


class SimpleHillClimbing(HillClimbing):
    def __init__(self, graph=None, objective_func = types.FunctionType):
        super().__init__(graph, objective_func)

    def get_next_state(self, state):
        current_objective = self.objectiveFunction(state)
        next_state = None
        next_max_objective = -1.0
        for child,_ in self.graph[state]:
            child_objective = self.objectiveFunction(child)
            if child_objective > next_max_objective:
                next_max_objective = child_objective
                next_state = child

        if next_state is not None and next_max_objective <= current_objective:
            return None
        return next_state