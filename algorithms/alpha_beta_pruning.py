import math


class AbstractNode:
    """
    parameters which are for representing state of the node must be implemented in overrided class of Node
    """

    def __init__(self, alpha, beta, utility_value, parent=None):
        self.alpha = alpha
        self.beta = beta
        self.utility_value = utility_value
        self.parent = parent

    def __lt__(self, other):
        if self.utility_value <= other.utility_value:
            return self

    def __gt__(self, other):
        if self.utility_value >= other.utility_value:
            return self


class AbstractAlgoConfigurator:
    """
    abstract configuration class

    utility_function(self) -> define the utility function to calculate the utility value for each node.
    get_successors(self)   -> take a node and expand it to reach the successors then return successors as a list.
    terminal_test(self)    -> check if state of the node is terminal else return -2. then if first player has worn return 1 but if
                              it has lost return -1 else if it's a draw return 0
    """

    def __init__(self, max_depth):
        self.max_depth = max_depth

    def utility_function(self) -> float:
        pass

    def terminal_test(self, node: AbstractNode) -> int:
        pass

    def get_successor(self, node: AbstractNode, is_maximizer=False):
        pass


class AlphaBetaPruning:
    """
    AlphaBetaPruning algorithm implementation based on abstraction that make it very flexible to be implemented for any
    custom problem like Tic-Tac-Toe like the example in problem directory. the implementation is suited for two-player
    games.

    it has two special function which is:
    minimizer(self)     -> take node, expand the successors, and select the best fitted node by looking forward in
    search tree. by best fitted node i meant to select a successor which result in providing best or at least better
    situation for minimizer player of the game.
    maximizer(self)     -> exact the same functionality of minimizer implemented for maximizer player of the game.
    """
    def __init__(self, initial_node: AbstractNode, conf: AbstractAlgoConfigurator):
        self.initial_node = initial_node
        self.conf = conf

    def minimizer(self, node: AbstractNode, depth=1):
        if depth > self.conf.max_depth:
            return node
        terminal_test_value = self.conf.terminal_test(node)
        if terminal_test_value != -2:
            node.utility_value = terminal_test_value
            return node
        next_node = AbstractNode(0, 0, utility_value=math.inf)
        successors, change_logs = self.conf.get_successor(node, False)
        for s in successors:
            print(f'node:\n{s}\n')
            maxi_res = self.maximizer(s, depth=depth + 1)
            maxi_node = maxi_res[0] if isinstance(maxi_res, (str, list, tuple)) else maxi_res
            if maxi_node.utility_value <= next_node.utility_value:
                next_node = s
                changed_house = change_logs[successors.index(s)]
            """checking for alpha-cut"""
            if next_node.utility_value <= node.alpha or next_node.alpha >= next_node.beta:
                return next_node, changed_house
            node.beta = min(node.beta, next_node.utility_value)
        print("___________")
        return next_node, changed_house

    def maximizer(self, node: AbstractNode, depth=1):
        if depth > self.conf.max_depth:
            return node
        terminal_test_value = self.conf.terminal_test(node)
        if terminal_test_value != -2:
            node.utility_value = terminal_test_value
            return node
        next_node = AbstractNode(0, 0, utility_value=-math.inf)
        successors, change_logs = self.conf.get_successor(node, True)
        for s in successors:
            mini_res = self.minimizer(s, depth=depth + 1)
            mini_node = mini_res[0] if isinstance(mini_res, (str, list, tuple)) else mini_res
            if mini_node.utility_value >= next_node.utility_value:
                next_node = mini_node
                changed_house = change_logs[successors.index(s)]
            """ checking for beta-cut """
            if next_node.utility_value >= node.beta or next_node.alpha >= next_node.beta:
                return next_node, changed_house
            next_node.alpha = max(node.alpha, next_node.utility_value)

        return next_node, changed_house
