from collections import deque
from utils import toggle, is_goal, state_to_tuple

def bfs(initial):
    queue = deque([(initial, 0)])
    visited = set()

    while queue:
        state, steps = queue.popleft()

        if is_goal(state):
            return steps

        key = state_to_tuple(state)
        if key in visited:
            continue
        visited.add(key)

        n = len(state)
        for i in range(n):
            for j in range(n):
                new_state = toggle(state, i, j)
                queue.append((new_state, steps + 1))

    return -1
