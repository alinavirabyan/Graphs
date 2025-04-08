def warshall_floyd():
    V = int(input("Մուտքագրեք գագաթների քանակը: "))
    graph = {i: [] for i in range(V)}
    E = int(input("Մուտքագրեք կապերի քանակը: "))
    
    print("Մուտքագրեք կապերը (գագաթ 1, գագաթ 2, կշիռ):")
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    
    matrix = [[float('inf')] * V for _ in range(V)]
    
    for u in graph:
        for v, weight in graph[u]:
            matrix[u][v] = weight

    for i in range(V):
        matrix[i][i] = 0
    
    print("Առաջին D^0 (սկզբնական մատրից):")
    for row in matrix:
        print(row)

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
        
        print(f"\nD^{k+1}:")
        for row in matrix:
            print(row)

warshall_floyd()
