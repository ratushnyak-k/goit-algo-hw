import heapq


def min_cost_to_connect_cables(cables):
    if len(cables) <= 1:
        return 0

    heap = cables[:]
    heapq.heapify(heap)

    total_cost = 0

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        cost = first + second
        total_cost += cost

        heapq.heappush(heap, cost)

    return total_cost


if __name__ == "__main__":
    cables = [4, 3, 2, 6]
    print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))