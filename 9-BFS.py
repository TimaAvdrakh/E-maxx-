def bfs(graph, s):
    visited ={}
    queue = []

    visited[s] = True
    queue.append(s)

    while queue:
        s = queue.pop(0)
        visited[s] = True
        print(s)
        for i in graph[s]:
            queue.append(i)

graph = {}
graph['tima'] = ['alesha','kuka']
graph['alesha'] = []
graph['kuka'] = ['almas', 'aidun','ali']
graph['almas'] = ['dias']
graph['dias'] = []
graph['aidun'] = []
graph['ali'] = []
name = 'tima'

bfs(graph,name)

