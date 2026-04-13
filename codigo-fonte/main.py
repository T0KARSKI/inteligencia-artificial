from bfs import bfs
from dfs import dfs
from astar import astar
from greedy import greedy
from hill_climbing import hill_climbing

# Exemplo simples de estado inicial (3x3)
initial_state = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

print("Resultados")
print("BFS:", bfs(initial_state))
print("DFS:", dfs(initial_state))
print("A*:", astar(initial_state))
print("Greedy:", greedy(initial_state))
print("Hill Climbing:", hill_climbing(initial_state))
