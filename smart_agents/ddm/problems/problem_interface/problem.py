from abc import ABC, abstractmethod

class Problem(ABC):

    @abstractmethod
    def get_random_future_state(self):
        pass

    @abstractmethod
    def get_all_future_states(self,state) -> list:
        pass

    @abstractmethod
    def validate_state(self):
        pass

    @classmethod
    def heuristic(cls, state):
        pass

    @abstractmethod
    def get_initial_state(self):
        pass

    @abstractmethod
    def get_current_state(self):
        pass

    @abstractmethod
    def update_current_state(self, state):
        pass

    @abstractmethod
    def get_goal_state(self) -> list:
        pass
    
    @abstractmethod
    def get_applicable_actions(self,state) -> list:
        pass

    def is_applicable(self,action,state):
        pass