import heapq


def dijkstra(graph: dict, start: str) -> dict:
    """
    graph: {вершина: [(сусід, вага), ...]}
    Повертає словник найкоротших відстаней від start до всіх вершин.
    """
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


if __name__ == "__main__":
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("C", 5), ("D", 10)],
        "C": [("E", 3)],
        "D": [("F", 11)],
        "E": [("D", 4), ("F", 6)],
        "F": [],
    }

    start_node = "A"
    result = dijkstra(graph, start_node)

    print(f"Найкоротші шляхи від вершини '{start_node}':")
    for node, dist in sorted(result.items()):
        print(f"  {start_node} -> {node}: {dist}")