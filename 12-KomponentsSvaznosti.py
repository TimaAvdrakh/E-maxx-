
from collections import defaultdict
used = defaultdict(bool)
graph = {}
arr = []
count = 0
def dfs(graph, vertex):
    if used[vertex] == False:
        arr.append(vertex)
        used[vertex] == True
        for i in graph[vertex]:
            if used[i] == False:
                dfs(graph,i)

def findComponent():
    for i in graph.keys():
        if used[i] == False:
            arr.clear()
            dfs(graph, i)

            print("Component " + str(count))
            count += 1
            for i in arr:
                print(i + " ")
