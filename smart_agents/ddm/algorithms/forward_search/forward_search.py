import random
from ...problems.problem_interface import Problem

class ForwardSearch:

    def __init__(self, general_functions: Problem):
        self.problem = general_functions

    def find_plan(self):
        
        problem = self.problem
        plan = []
        state = problem.get_initial_state()
        goal = problem.get_goal_state()
        applicable_actions = []
        
        while True:
            
            if state == goal:
                return plan
            
            applicable_actions = problem.get_applicable_actions(state)
            
            if applicable_actions == []:
                return "Failure"
            
            action = random.choice(applicable_actions)
            
            state = action(state) 
            plan.append(action)
