import copy
import math

from algorithms.alpha_beta_pruning import AbstractNode, AbstractAlgoConfigurator


class Node(AbstractNode):
    """
    state parameter is a 3*3 matrix which hold the game state.
    """

    def __init__(self, state, *args, **kwargs):
        if len(state) != 3 or len(state[0]) != len(state[1]) or len(state[1]) != len(state[2]):
            raise ValueError('node state must be matrix of 3*3!')
        self.state = state
        super(Node, self).__init__(*args, **kwargs)

    """ 'X' for first player, 'O' for computer """

    def __str__(self):
        result = ''
        for i in range(0, len(self.state)):
            for j in range(0, len(self.state)):
                if self.state[i][j] == 0:
                    result += '- '
                elif self.state[i][j] == 1:
                    result += 'X '
                else:
                    result += 'O '
            result += '\n'
        return result

    def __eq__(self, other):
        return self.beta == other.beta and \
               self.alpha == other.alpha and \
               self.utility_value == other.utility_value and \
               self.state == other.state and \
               self.parent == self.parent


class AlgoConfig(AbstractAlgoConfigurator):

    def __init__(self, *args, **kwargs):
        super(AlgoConfig, self).__init__(*args, **kwargs)

    def get_successor(self, node, is_maximizer=False):
        successors = []
        change_log = []
        for i in range(0, len(node.state)):
            for j in range(0, len(node.state[i])):
                if node.state[i][j] == 0:
                    node.state[i][j] = 1 if is_maximizer else 2
                    next_state = copy.deepcopy(node.state)
                    node.state[i][j] = 0
                    next_node = Node(next_state, alpha=node.alpha, beta=node.beta, parent=node,
                                     utility_value=self.utility_function(next_state))
                    successors.append(next_node)
                    change_log.append([i, j])
        return successors, change_log

    def terminal_test(self, node):

        if all(elem == node.state[0][0] for elem in [node.state[1][1], node.state[2][2]]):
            if node.state[0][0] == 1:
                return 1
            elif node.state[0][0] == 2:
                return - 1

        if all(elem == node.state[0][2] for elem in [node.state[1][1], node.state[2][0]]):
            if node.state[0][2] == 1:
                return 1
            elif node.state[0][2] == 2:
                return -1

        for row in node.state:
            if all(elem == row[0] for elem in row):
                if row[0] == 1:
                    return 1
                elif row[0] == 2:
                    return - 1

        for col in range(0, len(node.state)):
            if all(elem == node.state[0][col] for elem in [node.state[1][col], node.state[2][col]]):
                if node.state[0][col] == 1:
                    return 1
                elif node.state[0][col] == 2:
                    return -1

        for row in node.state:
            if any(elem == 0 for elem in row):
                return -2

        return 0

    """
    for maximizer we must pay attention to minimizer taken points and remove every row, column and diameter that contains
    minimizer points, for minimizer we consider the opposite situation and solution
    """

    def utility_function(self, state):
        maximizer_value = 8
        minimizer_value = 8

        for checker_value in range(1, 3):
            if any(elem == checker_value for elem in [state[0][0], state[1][1], state[2][2]]):
                if checker_value == 2:
                    maximizer_value -= 1
                else:
                    minimizer_value -= 1

            if any(elem == checker_value for elem in [state[0][2], state[1][1], state[2][0]]):
                if checker_value == 2:
                    maximizer_value -= 1
                else:
                    minimizer_value -= 1

            for row in state:
                if any(elem == checker_value for elem in row):
                    if checker_value == 2:
                        maximizer_value -= 1
                    else:
                        minimizer_value -= 1

            for col in range(0, len(state)):
                if any(elem == checker_value for elem in [state[0][col], state[1][col], state[2][col]]):
                    if checker_value == 2:
                        maximizer_value -= 1
                    else:
                        minimizer_value -= 1

        return maximizer_value - minimizer_value


