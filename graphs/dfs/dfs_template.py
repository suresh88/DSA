from tkinter import N


visited = [-1]*n 

def dfs(source):
    visited[source] = 1
    for neighbor in adjList[source]:
        if visited[neighbor] == -1:
            dfs(neighbor)
    ]