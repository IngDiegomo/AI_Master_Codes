import random
from ...problems.problem_interface import Problem

class Node:

    def __init__(self, plan:list, state, parent = None, children= None, general_functions = Problem):
        
        self.plan = plan
        self.state = state
        self.parent = parent
        self.children = children
        self.problem = general_functions
        self.heuristic = self.problem.heuristic(self.state)

    def __eq__(self, other) -> bool:
        
        return (
             self.__class__ == other.__class__ and
             tuple(self.state) == tuple(other.state)
         )

    def __hash__(self) -> int:
        
        return hash(tuple(self.state))
        
class DeterministicSearch:

    def __init__(self, general_functions: Problem):
        self.problem = general_functions
        

    def find_plan(self):
        
        problem = self.problem
        initial_node = Node(plan=[],state=problem.get_initial_state())
        goal = problem.get_goal_state()
        frontier = {initial_node}
        expanded = set()

        while (len(frontier) != 0):

            node = random.choice(list(frontier))
            expanded.add(node)
            frontier.remove(node)
            
            if node.state == goal:
                return node.plan 
            
            node.children = {Node(plan = node.plan + [action], state = action(node.state), parent = node) # type: ignore
                             for action in problem.get_applicable_actions(node.state)}
            
            node.children.difference_update(frontier.intersection(expanded))
            frontier = frontier.union(node.children)
            
        return "failure"