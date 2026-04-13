from utils import toggle, is_goal

def heuristic(state):
    return sum(cell == 0 for row in state for cell in row)

def hill_climbing(initial):
    state = initial
    steps = 0

    while True:
        if is_goal(state):
            return steps

        current_h = heuristic(state)
        best_state = None

        n = len(state)
        for i in range(n):
            for j in range(n):
                new_state = toggle(state, i, j)
                if heuristic(new_state) < current_h:
                    best_state = new_state
                    break

        if best_state is None:
            return -1

        state = best_state
        steps += 1
