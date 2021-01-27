import math

from algorithms.astar import AbstractNode, AbstractAlgoConfigurator, Astar, AbstractEvaluationFunc


class Node(AbstractNode):

    def __init__(self, row=math.inf, col=math.inf, *args, **kwargs):
        self.row = row
        self.col = col
        super(Node, self).__init__(*args, **kwargs)

    def __str__(self):
        return 'row: ' + str(int(self.row / 2)) + '| ' + \
               'col: ' + str(int(self.col / 2)) + '| ' + \
               ('parent: [ ' + f'{str(self.parent)} ]| '
                if not self.parent else '[row: ' \
                                        + str(int(self.parent.row / 2)) + ' col: '
                                        + str(int(self.parent.col / 2)) + ']| ') + \
               'step cost: ' + str(self.step_cost) + '| ' + \
               'path cost: ' + str(self.path_cost) + '| ' + \
               'heuristic value: ' + str(self.heu_value) + '| ' + \
               'evaluation value: ' + str(self.get_evaluation_value()) + '| '


class MazeAlgoConfig(AbstractAlgoConfigurator):
    """
    env is 2 dimention array with 2n+1 row and col so we can mention walls within env
    """

    def __init__(self, env, goal_row, goal_col):
        if not isinstance(env, list):
            raise TypeError('env must be 2 dimention list')
        self.env = env
        self.goal_row = goal_row
        self.goal_col = goal_col

    def calc_heuristic(self, row, col):
        ## TODO : check the floor function out later
        return math.floor((abs(self.goal_row - row) + abs(self.goal_col - col)) / 2)

    def get_successors(self, node):
        successors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if abs(i) != abs(j) \
                            and self.env[node.row + i][node.col + j] != 1 \
                            and node.row + 2 * i > -1 \
                            and node.col + 2 * j > -1:
                        row = node.row + 2 * i
                        col = node.col + 2 * j
                        if node.parent is not None and (node.parent.row == row and node.parent.col == col):
                            continue
                        successors.append(
                            Node(row=row, col=col, parent=node, heuristic_value=self.calc_heuristic(row, col),
                                 path_cost=node.path_cost + 1, step_cost=1))
                except:
                    pass
        return successors

    def goal_test(self, node):
        if node.row == self.goal_row and node.col == self.goal_col:
            return True
        return False


class MazeEvaluationFunc(AbstractEvaluationFunc):

    def get_next(self, open_list) -> AbstractNode:
        open_list.sort(key=lambda x: x.get_evaluation_value())
        return open_list[0]


env = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
]

config = MazeAlgoConfig(env=env, goal_row=14, goal_col=18)
evaluation_func = MazeEvaluationFunc()
initial_node = Node(0, 0, heuristic_value=config.calc_heuristic(0, 0), path_cost=0, step_cost=1)

a_star_search_instance = Astar(initial_node, config, evaluation_func)
a_star_search_instance.search(True)
