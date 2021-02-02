# artificial-intelligence-project
Academic project of artificial-intelligence course.
Implementing three important algorithm of: 
- **A-Star** 
-  **simulated Annealing** 
- **Alpha-Beta-Pruning** 

with one usage example for each.
## Algorithms Description
### A-Star
**A*** (pronounced "A-star") is a graph traversal and path search  algorithm, which is often used in many fields of computer science due to its completeness, optimality, and optimal efficiency. One major practical drawback is its ![O(b^d)](https://wikimedia.org/api/rest_v1/media/math/render/svg/c99d691c81f015266d1626ef381d2a1a49466fbb) space complexity, as it stores all generated nodes in memory. A* selects the path that minimizes

![f(n)=g(n)+h(n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/5c05c9af6fa9d56e8faf12460bf98ebf9f936581)
where  n  is the next node on the path,  _g_(_n_)  is the cost of the path from the start node to  n, and  _h_(_n_)  is a  heuristic function that estimates the cost of the cheapest path from  n  to the goal.

![A-Star flowchart](https://github.com/arvin2079/artificial-intelligence-project/blob/master/media/Flow-chart-of-A-star-algorithm.png)

### Simulated-Annealing
**Simulated annealing** (**SA**) is a probabilistic for approximating the global optimum of a given function. Specifically, it is a metaheuristic to approximate global optimization in a large search space for an optimization problem. 
The state of some physical systems, and the function _E_(_s_) to be minimized, is analogous to the internal energy of the system in that state. The goal is to bring the system, from an arbitrary _initial state_, to a state with the minimum possible energy.

![SA implementation on hillclimbing](https://github.com/arvin2079/artificial-intelligence-project/blob/master/media/Hill_Climbing_with_Simulated_Annealing.gif)

###  α-β Pruning
**Alpha–beta pruning** algorithm implementation based on abstraction that make it very flexible to be implemented for any custom problem like Tic-Tac-Toe like the example in problem directory. the implementation is suited for two-player games. It stops evaluating a move when at least one possibility has been found that proves the move to be worse than a previously examined move. Such moves need not be evaluated further. When applied to a standard minimax tree, it returns the same move as minimax would, but prunes away branches that cannot possibly influence the final decision.

![minimax with alpha beta pruning](https://github.com/arvin2079/artificial-intelligence-project/blob/master/media/20090615232625!Minmaxab.gif)

## Algorithms Implementation Description
### A-Star
Astar class take three object of initial_node, configuration and evaluation_function. also has two function of *has_more_node(self)*  for checking if is there any node in open_list or not and *search(self, print_attempts)* which is logic class of A* algorithm implementation. in saerch function you can set print_attempts to True thus search logs would be printed in terminal while the algorithm is working.

> if search function return None it means search failed

related Abstract classes:
- AbstractNode
- AbstractAlgoConfigurator
- AbstractEvaluationFunc

### SA
SimulatedAnnealing class take three object of initial_state, configuration and minimize. minimize by default is False but you can set minimize to True if you want SA algorithm to search for global minimum. in saerch function of the class you can set print_attempts to True thus search logs would be printed in terminal while the algorithm is working.
related Abstract classes:
- AbstractState
- AbstractAlgoConfigurator
### α-β Pruning
AlphaBetaPruning class take two object of initial_node and configuration.
it has two special function which is:  
- *minimizer(self)*     -> take node, expand the successors, and select the best fitted node by looking forward in  
search tree. by best fitted node i meant to select a successor which result in providing best or at least better  
situation for minimizer player of the game.  
- *maximizer(self)*     -> exact the same functionality of minimizer implemented for maximizer player of the game.

related Abstract classes:
- AbstractNode
- AbstractAlgoConfigurator

## Examples Implementation Description
### Maze Problem
for the simulation of **n × n** maze environment we would consider a matrix with **2n -1** rows and columns. in the mentioned matrix every two house of maze env are separated from each other by on house intended to shown obstacles (***1** for closed ways or walls and **0** for the ways that are open*). the general approach is overriding abstract and predefined classes of A* algorithm which I have been written before.
- **Node**: overriding AbstractNode Class with two additional arguments of **row** and **col** which indicate the state of the node in the environment matrix
- **MazeAlgoConfig**: overriding AbstractAlgoConfigurator Class which take the maze enviroment as a matrix that has been described earlier and also goal node information (goal_row, goal_col).
- **MazeEvaluationFunc**: overriding AbstractEvaluationFunc Class which take open_list of A* and then return the node with best evaluation value.
### 8 Queen Problem
a **8 × 8** matrix is considered for this problem which is defined as queens_state and it is a parameter of State class 
- **State**: overriding AbstractState Class with additional argument of queens_state which explained earlier. each State object shows one special stage of algorithm iteration.
- **AlgoConfig**: overriding AbstractAlgoConfigurator Class which is set of configuration that must be implemented (e.g. heuristic calculator, successor generator and goal test function).
### Tic-Tac-Toe
Tkinter is used for the game environment simulation which is a python GUI toolkit. the environment  is a **3 × 3** matrix that is shown to the player. Player moves would be marked with **X** and computer moves would be marked with **O**.
In the `problems\tic_tac_toe` the implementation of game is consist of two separate part one is the GUI [*tic_tac_toe_gui.py*] and the second is the logic [*implemented_algorithm.py*].
Logic part is consist of classes below :
- **Node**: overriding AbstractNode Class which has an argument called state that is representation of game state. state is a **3 × 3** matrix in which computer movements with 2 and player movements with 1 are shown and the blank houses are 0. 
- **AlgoConfig**: overriding AbstractAlgoConfigurator Class which is set of configuration that must be implemented. it take max_depth argument Which is used to limit memory consumption.
	- *get_successor(self, node, is_maximizer) -> list:* take node and is_maximizer and then return list of successor for that node, if is_maximizer was True it would return list of successor for maximizer node else return for minimizer node.
	- *terminal_test(self, node) -> int*: take a node and check if it is terminal or not.if the state is one the *draw, win, or lose* it would detect and then return 1 for win, -1 for lose and 0 for draw else if none, return -2.
	- *utility_function(self) -> float*: take the node state and return the utility value by subtracting possible ways of winning for minimizer or computer from possible ways of winning for maximizer or player.

## MIT License

Copyright (c) 2021 ArvinSadeghi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contribute
Feel Free to contribute or use any part of this project in your own projects just dont forget to send feedback to me ;)
