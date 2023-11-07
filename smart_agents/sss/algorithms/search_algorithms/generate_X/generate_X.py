from .. import helper_functions as hp
from ....problems.problem_interface import Problem

class GenerateX:

    def __init__(self, general_functions: Problem):
        self.problem = general_functions

    def find_solution(self):
        
        problem = self.problem
        goal = [problem.get_goal_state()]
        Fr = [problem.get_initial_state()]
        newFr = [problem.get_initial_state()]
        X = [problem.get_initial_state()]
        

        while not (any ([state in Fr for state in goal])):

            for state in Fr:                 
                for next_state in problem.get_all_future_states(state): 
                    newFr.append(next_state)  
            
            Fr = Fr + newFr 
            Fr = hp.remove_duplicates(Fr)
            X = X + Fr 
            newFr = []

        return X, 