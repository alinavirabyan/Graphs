def queue(edges, inp):
    queue = []
    visited = []
    queue.append(inp)
    visited.append(inp)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for edge in edges:
            if node == edge[0] and edge[1] not in visited:
                queue.append(edge[1])
                visited.append(edge[1])
            elif node == edge[1] and edge[0] not in visited:
                queue.append(edge[0])
                visited.append(edge[0])

def result(edges):
    inp = int(input('Input a number: '))
    print("Starting BFS traversal from node", inp)
    queue(edges, inp)

edges = [[4, 3], [3, 1], [3, 8], [2, 8]]

result(edges)
