
DIVIDER_LINE = '__________________________________________________________________________________________________________'

class AbstractNode:
    """
    Astar node model, can be expanded for different problems
    step_cost is cost of path from parent to current node.
    """

    def __init__(self, heuristic_value, path_cost, step_cost, parent=None):
        self.heu_value = heuristic_value
        self.path_cost = path_cost
        self.parent = parent
        self.step_cost = step_cost

    def get_evaluation_value(self):
        return self.path_cost + self.heu_value

    def print_path_trace(self, total_step_taken):
        if self.parent and total_step_taken > 0:
            self.parent.print_path_trace(total_step_taken-1)
        print(f'\t{total_step_taken}- {self}')


class AbstractAlgoConfigurator:
    """
    abstract configuration class

    calc_heuristic(self) -> define heuristic function to calculate heuristic based on optional method.
    get_successors(self) -> take a node and expand it to reach the successors then return successors as a list.
    goal_test(self)      -> implement for algorithm is_goal checking.
    """

    def calc_heuristic(self):
        pass

    def get_successors(self, node) -> list:
        pass

    def goal_test(self, node) -> bool:
        pass


class AbstractEvaluationFunc:
    """
    abstract Evaluation function class take list of nodes and return most evaluated
    node, must be expanded for different problems.
    in saerch function you can set print_attempts to True thus search logs would be printed in terminal while the
    algorithm is working.

    get_next(self) -> implement to retrive "next_evaluated_node"
    """

    def get_next(self, open_list: list) -> AbstractNode:
        pass


class Astar:
    """
    A-star algorithm implementation
    if search function return None --> search failed
    """

    def __init__(self, initial_node: AbstractNode, config, evaluation_func):
        self.open_list = [initial_node, ]
        if isinstance(config, AbstractAlgoConfigurator):
            self.config = config
        else:
            raise TypeError('heuristic fucntion must be subtype of AbstractHeuristicFunc class')

        if isinstance(evaluation_func, AbstractEvaluationFunc):
            self.evaluation_func = evaluation_func
        else:
            raise TypeError('evaluation fucntion must be subtype of AbstractEvaluationFunc class')

    def has_more_node(self):
        return len(self.open_list) > 0

    def search(self, print_attempts: bool):
        while self.has_more_node():
            next_node = self.evaluation_func.get_next(self.open_list)

            if self.config.goal_test(next_node):
                if print_attempts:
                    print(f'FOUND!\ngoal : \n\t{next_node}')
                    print('path:')
                    next_node.print_path_trace(next_node.path_cost)

                return next_node

            if next_node in self.open_list:
                self.open_list.remove(next_node)

            successors = self.config.get_successors(next_node)
            self.open_list.extend(successors)

            if print_attempts:
                print(f'current node :\n\t{next_node}')
                print('open list :')
                for item in self.open_list:
                    print(f'\t{item}')
                print(DIVIDER_LINE)
        if print_attempts:
            print('FAILED!')
        return None
