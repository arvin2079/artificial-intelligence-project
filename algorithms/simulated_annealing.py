import math
import random

DIVIDER_LINE = '__________________________________________'

class AbstractState:
    """
    abstract node which has to be completed for each problem individually
    """

    def __init__(self, heuristic_value):
        self.heuristic_value = heuristic_value


class AbstractAlgoConfigurator:
    """
    abstract configuration class

    calc_heuristic(self)        -> define heuristic function to calculate heuristic based on optional method.
    get_random_successors(self) -> take a state and return new random state from that state.
    goal_test(self)             -> implement for algorithm is_goal checking.
    """

    def __init__(self, initial_temp, temp_step):
        self.initial_temp = initial_temp
        self.temp_step = temp_step

    def calc_heuristic(self):
        pass

    def get_random_successors(self, state) -> list:
        pass

    def goal_test(self, state) -> bool:
        pass


class SimulatedAnnealing:

    def __init__(self, conf: AbstractAlgoConfigurator, initial_state, minimize=False):
        self.conf = conf
        self.initial_state = initial_state
        self.minimize = minimize

    """
    if minimize is "TRUE" then the algorithm will search for universal minimum value
    and "FALSE" for maximizing. 
    in saerch function you can set print_attempts to True thus search logs would be printed in terminal while the 
    algorithm is working.
    """

    def search(self, print_attempts=False):
        temp = self.conf.initial_temp
        current_state = self.initial_state

        counter = 1

        if print_attempts:
            print('STEP 0:')
            print(f'temp: {temp}')
            print(f'temp step: {self.conf.temp_step}')
            print(current_state)
            print(DIVIDER_LINE)

        while temp > 0:
            next_state = self.conf.get_random_successors(current_state)

            energy_variation = (next_state.heuristic_value - current_state.heuristic_value) * (
                1 if not self.minimize else -1)
            if energy_variation > 0:
                current_state = next_state
                if print_attempts:
                    print(f'STEP {counter}:')
                    print(f'temp: {temp}')
                    print('ΔE > 0')
                    print(f'energy variation: {energy_variation}')
                    print(current_state)
                    print(DIVIDER_LINE)
                counter += 1
                temp -= self.conf.temp_step
                continue

            prob = math.pow(math.e, energy_variation / temp)
            random_number = random.uniform(0, 1)
            if random_number < prob:
                current_state = next_state
            if print_attempts:
                print(f'STEP {counter}:')
                print('ΔE < 0')
                print(f'temp: {temp}')
                print(f'energy variation: {energy_variation}')
                print(f'probability: {prob}')
                print(f'random number (0,1): {random_number}')
                print('STEP TAKEN' if random_number < prob else 'STEP NOT TAKEN')
                print(current_state)
                print(DIVIDER_LINE)
            counter += 1
            temp -= self.conf.temp_step
        if print_attempts:
            print(f'STEP {counter}:')
            print(f'temp: {temp + self.conf.temp_step}')
            print(f'temp step: {self.conf.temp_step}')
            print('FINAL STATE: ')
            print(current_state)
            print(DIVIDER_LINE)
        return current_state, self.conf.goal_test(current_state), counter
