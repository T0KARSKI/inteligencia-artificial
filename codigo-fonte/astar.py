import heapq
from utils import toggle, is_goal, state_to_tuple

def heuristic(state):
    return sum(cell == 0 for row in state for cell in row)

def astar(initial):
    heap = [(heuristic(initial), 0, initial)]
    visited = set()

    while heap:
        _, cost, state = heapq.heappop(heap)

        if is_goal(state):
            return cost

        key = state_to_tuple(state)
        if key in visited:
            continue
        visited.add(key)

        n = len(state)
        for i in range(n):
            for j in range(n):
                new_state = toggle(state, i, j)
                new_cost = cost + 1
                priority = new_cost + heuristic(new_state)

                heapq.heappush(heap, (priority, new_cost, new_state))

    return -1
