import random
import copy

class SlidingPuzzle():

    def __init__(self , n , m):
        
        self.n = n
        self.m = m
        self.grid = list(range(1, n*m))
        self.goal = list(range(1,n*m))
        random.shuffle(self.grid)
        self.grid.append(0)
        self.goal
        self.transitions = [-self.m , self.m , -1 , 1]
        
    
    def __str__(self) -> str:
        
        left_values = [x*self.m for x in range(0,self.m)]
        right_values = [(x*self.m)-1 for x in range(1,(self.m)+1)]

        string_grid = "" 
        
        for i in range (0,self.n*self.m):
            if i in left_values:
                string_grid += "   " + str(self.grid[i])
            elif i in right_values:
                string_grid += "    ,   " + str(self.grid[i]) + "   \n"
            else:
                string_grid += "   ,   " + str(self.grid[i]) 
        
        return string_grid



def valid(state:SlidingPuzzle , i , d):
        
        if (0<=d<=3):
            
            i += state.transitions[d] 
            
            if (0<=i<=((state.n*state.m)-1)): return True
                 
        
        return False
    

def action(state:SlidingPuzzle , d):
        
        for i in range(0,state.n*state.m):

            if ((state.grid[i] == 0) and (valid(state,i,d))):

                new_state = copy.deepcopy(state)

                new_state.grid[i] = state.grid[i + state.transitions[d]]
                new_state.grid[i + state.transitions[d]] = 0
                
                return new_state
        
        print("Not valid action d = " + str(d))
        return state

def T(state : SlidingPuzzle) -> list:
    
    options = []

    for i in range(len(state.transitions)):

        new_state = action(state,i)
        if (new_state.grid != state.grid):
            options.append(new_state)
             
    return options


