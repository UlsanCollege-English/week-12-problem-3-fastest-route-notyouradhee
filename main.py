import heapq


def dijkstra_shortest_path(graph, start, goal):
    """
    Compute the shortest path in a graph with positive edge weights.

    graph: dict mapping node -> list of (neighbor, weight) pairs.
    start: starting node (string).
    goal: target node (string).

    Return:
        (path, total_cost)
        - path: list of nodes from start to goal with minimum total weight
        - total_cost: sum of weights along the path
        If start/goal is not in graph or goal is unreachable, return ([], None).
    """
    # TODO Step 1: Briefly write what this function should compute.
    # TODO Step 2: Re-phrase the problem in simple English in a comment.
    # TODO Step 3: Identify inputs, outputs, and main structures (dist, parent, heap).
    # TODO Step 4: Plan Dijkstra: how to update distances and parents.
    # TODO Step 5: Write pseudocode for Dijkstra using a priority queue (heap).
    # TODO Step 6: Translate your pseudocode into Python with heapq.
    # TODO Step 7: Test with small graphs where you know the correct answer.
    # TODO Step 8: Check that your solution's complexity is about O((V + E) log V).

    if start not in graph or goal not in graph:
        return ([], None)
    
    if start == goal:
        return ([start], 0)
    
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    parent = {}
    heap = [(0, start)]
    
    while heap:
        current_dist, node = heapq.heappop(heap)
        
        if current_dist > dist[node]:
            continue
        
        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))
    
    if dist[goal] == float('inf'):
        return ([], None)
    
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    
    return (path, dist[goal])


if __name__ == "__main__":
    # Optional quick check
    sample_graph = {
        "K1": [("K2", 5), ("K3", 2)],
        "K2": [("K1", 5), ("K4", 4)],
        "K3": [("K1", 2), ("K4", 7)],
        "K4": [("K2", 4), ("K3", 7)],
    }
    path, cost = dijkstra_shortest_path(sample_graph, "K1", "K4")
    print("Sample path from K1 to K4:", path, "cost:", cost)
