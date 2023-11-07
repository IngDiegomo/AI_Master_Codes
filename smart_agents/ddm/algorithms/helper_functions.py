def apply_plan(plan, state):
    
    for action in plan:
        state = action(state)

    return state
