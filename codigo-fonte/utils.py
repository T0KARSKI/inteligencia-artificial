def toggle(state, x, y):
    n = len(state)
    new_state = [row[:] for row in state]

    directions = [(0,0),(1,0),(-1,0),(0,1),(0,-1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            new_state[nx][ny] ^= 1

    return new_state


def is_goal(state):
    return all(cell == 1 for row in state for cell in row)


def state_to_tuple(state):
    return tuple(tuple(row) for row in state)
