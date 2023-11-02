from ast import FunctionType
from types import MethodType
from representation import SlidingPuzzle
import helper_functions as hp

def generateX(s_0:SlidingPuzzle, G:SlidingPuzzle , T):

    X = Fr = newFr = [s_0]

    while (hp.list_intersection(Fr,G)==[]):

        for state in Fr:
            for next_state in T(state):
                newFr.append(next_state)

        Fr.append(newFr)
        Fr = hp.remove_duplicates(Fr)
        X.append(Fr)
        newFr = []
   
    return X
    
