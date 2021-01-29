import copy
import random

from algorithms.simulated_annealing import AbstractState, AbstractAlgoConfigurator, SimulatedAnnealing


class State(AbstractState):
    """
    this node is just for 8 queen problem but can be expanded easily for n-queen you just have to override
    these classes and their functions.
    """

    def __init__(self, queens_state, *args, **kwargs):
        self.queens_state = queens_state
        if len(queens_state) != 8:
            raise ValueError('state length must be 8!')
        for item in queens_state:
            if item is None or item > 7 or item < 0:
                raise ValueError(f'element [ {item} ] in state list is not allowed!')
        super(State, self).__init__(*args, **kwargs)

    def __str__(self):
        result = f'heuristic value: {self.heuristic_value}\n'

        for i in range(0, len(self.queens_state)):
            line = ''
            for j in range(0, len(self.queens_state)):
                if self.queens_state[j] == i:
                    line += 'X '
                else:
                    line += '- '
            result += line + '\n'
        return result


class AlgoConfig(AbstractAlgoConfigurator):

    def calc_heuristic(self, queens_state):
        heuristic_value = 0
        for col_num in range(0, 8):
            for j in range(1, 8):
                if queens_state[(j + col_num) % 8] == queens_state[col_num]:
                    heuristic_value += 1

            for k in range(1, 8):
                if abs(queens_state[col_num] - queens_state[(col_num + k) % 8]) == abs(col_num - ((col_num + k) % 8)):
                    heuristic_value += 1

        heuristic_value /= 2
        return int(heuristic_value)

    def get_random_successors(self, state: State):
        copied_state = copy.deepcopy(state)
        while True:
            rand_index = random.randint(0, 7)
            rand_value = random.randint(0, 7)
            if copied_state.queens_state[rand_index] == rand_value:
                continue
            copied_state.queens_state[rand_index] = rand_value
            copied_state.heuristic_value = self.calc_heuristic(copied_state.queens_state)
            return copied_state

    def goal_test(self, state):
        if self.calc_heuristic(state.queens_state) == 0:
            return True
        return False


initial_queens_state = [0, 0, 0, 0, 0, 0, 0, 0]

conf = AlgoConfig(initial_temp=10, temp_step=0.001)
initial_state = State(initial_queens_state, conf.calc_heuristic(initial_queens_state))

simulated_annealing_search_instance = SimulatedAnnealing(conf, initial_state, True)
simulated_annealing_search_instance.search(True)
