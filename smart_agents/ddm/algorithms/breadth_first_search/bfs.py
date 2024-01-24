from platform import node
import random
import select
from ...problems.problem_interface import Problem

class Node:

    def __init__(self, general_functions:Problem, plan:list, state, parent = None, children= None):
        
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
    
    def __str__(self) -> str:

        return str(self.state)
        
class BreadthFirstSearch:

    def __init__(self, general_functions: Problem):
        self.problem = general_functions

    def select(self,nodes):

        nodes = list(nodes)
        nodes.sort(key=lambda node: len(node.plan))

        for i in range(1,len(nodes)):
            if len(nodes[i].plan) == len(nodes[i-1].plan):
                nodes.sort(key=lambda node: (len(node.plan) + node.heuristic))
                return nodes[0]
        return nodes[0]

    def prune(self,children,frontier,expanded):

        to_remove = set()

        for expanded_node in expanded:    
        
            for children_node in children:

                if (expanded_node.state == children_node.state and
                    expanded_node.plan != children_node.plan):
                    to_remove.add(children_node)

        children.difference_update(to_remove)

        to_remove = set()

        for expanded_node in expanded:    
        
            for frontier_node in frontier:
                
                if (expanded_node.state == frontier_node.state and
                    expanded_node.plan != frontier_node.plan):
                    to_remove.add(frontier_node)
        
        frontier.difference_update(to_remove)
        
        return frontier, children

    def find_plan(self):
        
        problem = self.problem
        node = Node(general_functions=self.problem, plan=[], state=problem.get_initial_state())

        node.children = {Node(general_functions=problem,
                                      plan = node.plan + [action],
                                      state = action(node.state),
                                      parent = node)
                                      for action in problem.get_applicable_actions(node.state)}
        
        goal = problem.get_goal_state()
        frontier = node.children
        expanded = {node}
        
        while (len(frontier) != 0):

            node = self.select(frontier)

            expanded.add(node)
            frontier.remove(node)
            
            if node.state == goal:
                return node.plan 
            
            node.children = {Node(general_functions=problem,
                                  plan = node.plan + [action],
                                  state = action(node.state),
                                  parent = node) 
                                  for action in problem.get_applicable_actions(node.state)}
            
            
            #frontier, node.children = self.prune(node.children,frontier,expanded)
            
            node.children.difference_update(node.children.intersection(expanded))
            frontier.difference_update(frontier.intersection(expanded))

            frontier = frontier.union(node.children)

        print(len(node.plan))
        return "failure"