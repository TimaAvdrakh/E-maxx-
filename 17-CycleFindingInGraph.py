from collections import defaultdict
graph = { }
color = defaultdict(int)
parent = []

def dfs(graph, vertex):
    color[vertex] = 1
    for i in graph[vertex]:
        if color[i] == 0:
           parent[i] = vertex
           if (dfs(graph, vertex)):
               return True
        elif color[i] == 1:
            cycle_start = i
            cycle_end = vertex
            return True
    color[vertex] = 2
    return False


