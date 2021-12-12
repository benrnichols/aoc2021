f = open('input.txt', 'r')
def find_paths(node, path, cave_graph):
    if node == "end":
        return 1
    if node == "start" and len(path) > 1:
        return 0
    paths = 0
    for x in cave_graph[node]:
        if len(list(filter(lambda y: True if y.islower() and path.count(y) == 2 else False, path))) > 0 and x.islower() and x in path:
            continue
        else:
            paths += find_paths(x, path[:]+[x], cave_graph)
    return paths

cave_graph = {}
for x in f:
    x = x.rstrip()
    a,b = x.split('-')
    if a not in cave_graph:
        cave_graph[a] = []
    cave_graph[a].append(b)
    if b not in cave_graph:
        cave_graph[b] = []
    cave_graph[b].append(a)

print(cave_graph)
paths = 0
current = "start"
print(find_paths(current, ["start"], cave_graph))
