rebra = {}
graph = {}
weight = [100000000] * vertex.__len__()
from collections import deque
queue = deque()

def djistra(graph, vertex):
    queue.append(vertex)
    weight[vertex] = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            weight[i] = min(weight[i],weight[v]+rebra[v][i])
            queue.append(i)

