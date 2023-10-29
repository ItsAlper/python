def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    while graph:
        current_node = min(graph, key=lambda node: distances[node])
        
        for neighbor, weight in graph[current_node].items():
            potential_route = distances[current_node] + weight
            if potential_route < distances[neighbor]:
                distances[neighbor] = potential_route
        
        del graph[current_node]
    
    return distances

if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    
    start_node = 'A'
    
    distances = dijkstra(graph, start_node)
    
    print("Nejkratší vzdálenosti od počátečního uzlu ({})".format(start_node))
    for node, distance in distances.items():
        print("Uzel: {}, Nejkratší vzdálenost: {}".format(node, distance))
