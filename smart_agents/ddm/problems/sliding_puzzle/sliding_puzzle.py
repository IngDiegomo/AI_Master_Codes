from ..problem_interface import Problem
import random
import copy

class SlidingPuzzle(Problem):

    def __init__(self , n: int, m:int):
        
        self.n = n
        self.m = m
        self.initial_state = list(range(1, n*m))
        self.goal_state = list(range(1, n*m))
        random.shuffle(self.initial_state)
        self.initial_state.append(0)
        self.current_state = copy.deepcopy(self.initial_state)
        self.goal_state.append(0)
        self.actions = [self.movehole]
        self.transitions = [-self.m , self.m , -1 , 1]
        self.zero_index = len(self.initial_state) - 1
            
    def __str__(self) -> str:
        
        left_values = [x*self.m for x in range(0,self.m)]
        right_values = [(x*self.m)-1 for x in range(1,(self.m)+1)]

        string_grid = "" 
        
        for i in range (0,self.n*self.m):
            if i in left_values:
                string_grid += "   " + str(self.current_state[i])
            elif i in right_values:
                string_grid += "    ,   " + str(self.current_state[i]) + "   \n"
            else:
                string_grid += "   ,   " + str(self.current_state[i]) 
        
        return string_grid

    def movehole(self, d:int, state):
         
        action = lambda state, d = d: self.movehole(d,state)
        
        if not(self.is_applicable(action,state)):
            
            return state
        
        else:

            future_state = copy.deepcopy(state)
            future_state[state.index(0)] = state[state.index(0) + self.transitions[d]]
            future_state[state.index(0) + self.transitions[d]] = 0
            
            return future_state
                 
    
    def is_applicable(self, action, state):
        
        if (not(0<= action.__defaults__[0] <= len(self.transitions)-1) or 
            not(0<=(state.index(0) + self.transitions[action.__defaults__[0]]) <= ((self.n*self.m)-1))):

            return False
        
        return True
    
    def get_applicable_actions(self,state):
        
        applicable_actions = []
        
        for d in range(0,len(self.transitions)):
            action = lambda state, d = d, : self.movehole(d,state)
            if self.is_applicable(action,state):
                applicable_actions.append(action)
        
        return applicable_actions

    
    def get_random_future_state(self,state):
        
        while True:

            random_movement = random.randint(0,len(self.transitions)- 1)
            future_state = self.movehole(random_movement,state)

            if future_state != state:
                return future_state

    def get_all_future_states(self,state):
        
        future_states = [
            self.movehole(d,state)
            for d in range(0,len(self.transitions))
            if self.movehole(d,state) != state
        ]
    
        return  future_states
    
    @classmethod
    def heuristic(cls, state):
        
        non_ordered_numbers = 0
        goal_state = list(range(1, len(state)+1))
        goal_state.append(0) 
        
        for i in range (0, len(state)):
            if state[i] != goal_state[i]:
                non_ordered_numbers += 1
            
        return non_ordered_numbers
    
    def validate_state(self):
        return SlidingPuzzle.heuristic(self.current_state) == 0
    
    def get_initial_state(self) -> list:
        return self.initial_state
    
    def get_current_state(self) -> list: 
        return self.current_state
    
    def update_current_state(self, state):
        self.zero_index = state.index(0)
        self.current_state = state
    
    def get_goal_state(self) -> list:
        return self.goal_state

    def is_solvable(self,state):
        
        count = 0

        for i in range(0,(self.n*self.m)-1):
            for j in range(i+1, (self.n*self.m)):
                if state[j] and state[i] and state[i] > state[j]:
                    count += 1
        print(count)
        return count % 2 == 0    

