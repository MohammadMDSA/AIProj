import random
import types

from aI_fall2018_p2.search.search import Search


class SimulatedAnnealing(Search):

    objective_function = types.FunctionType
    MAX_TRY = 25

    def __init__(self, graph=None, objective_function=types.FunctionType):
        super().__init__(graph)
        self.objective_function = objective_function

    def search(self, start, goal):
        current_state = start
        n = 0
        try_num = 0

        while True:
            random_neighbour = random.choice(self.graph)

            if self.objective_function(random_neighbour) > self.objective_function(current_state) or current_state.get_possibility(n + try_num):
                current_state = random_neighbour
                n += 1
                try_num = 0
            else:
                try_num += 1
            if try_num >= self.MAX_TRY:
                break

        return current_state
