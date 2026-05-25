import uuid
from collections import deque
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def heap_to_tree(heap: list, index: int = 0):
    if index >= len(heap):
        return None
    node = Node(heap[index])
    node.left = heap_to_tree(heap, 2 * index + 1)
    node.right = heap_to_tree(heap, 2 * index + 2)
    return node


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree_colored(root, title="Обхід дерева"):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)
    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}
    plt.figure(figsize=(10, 6))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def generate_colors(n: int) -> list:
    """Кольори від темно-синього до світло-блакитного у hex."""
    colors = []
    for i in range(n):
        ratio = i / max(n - 1, 1)
        r = int(0 + ratio * 173)
        g = int(0 + ratio * 216)
        b = int(139 + ratio * (230 - 139))
        colors.append("#{:02X}{:02X}{:02X}".format(r, g, b))
    return colors


def dfs_iterative(root: Node) -> list:
    """DFS через стек, повертає вузли в порядку відвідування."""
    if root is None:
        return []
    visited = []
    stack = [root]
    while stack:
        node = stack.pop()
        visited.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return visited


def bfs_iterative(root: Node) -> list:
    """BFS через чергу, повертає вузли в порядку відвідування."""
    if root is None:
        return []
    visited = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        visited.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return visited


def colorize_and_draw(root, order: list, title: str):
    colors = generate_colors(len(order))
    for node, color in zip(order, colors):
        node.color = color
    draw_tree_colored(root, title=title)


if __name__ == "__main__":
    data = [1, 3, 5, 7, 10, 12, 15]
    heap = data[:]
    heapq.heapify(heap)

    # DFS
    root_dfs = heap_to_tree(heap)
    order_dfs = dfs_iterative(root_dfs)
    print("DFS порядок:", [n.val for n in order_dfs])
    colorize_and_draw(root_dfs, order_dfs,
                      "DFS - обхід у глибину (темний → світлий)")

    # BFS
    root_bfs = heap_to_tree(heap)
    order_bfs = bfs_iterative(root_bfs)
    print("BFS порядок:", [n.val for n in order_bfs])
    colorize_and_draw(root_bfs, order_bfs,
                      "BFS - обхід у ширину (темний → світлий)")