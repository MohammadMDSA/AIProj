import types

from aI_fall2018_p2.search.search import Search


class HillClimbing(Search):

    objectiveFunction = types.FunctionType

    def __init__(self, graph=None, objective_func=types.FunctionType):
        super().__init__(graph)
        self.objectiveFunction = objective_func

    def search(self, start, goal):
        curent_state = start
        next_state = None

        while True:
            next_state = self.get_next_state(curent_state)

            if next_state is not None:
                curent_state = next_state
            else:
                break
        return curent_state

    def get_next_state(self, state):
        pass
