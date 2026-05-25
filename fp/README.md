# Алгоритми та структури даних

## Структура проєкту

- `task1_singly_linked_list.py` - реверс, сортування та об'єднання однозв'язного списку
- `task2_pythagoras_tree.py` - побудова фрактала "дерево Піфагора"
- `task3_dijkstra_heap.py` - алгоритм Дейкстри з використанням бінарної купи
- `task4_heap_visualization.py` - візуалізація бінарної купи
- `task5_tree_traversal_visualization.py` - візуалізація обходів DFS і BFS
- `task6_food_knapsack.py` - жадібний алгоритм і динамічне програмування
- `task7_monte_carlo_dice.py` - метод Монте-Карло для двох кубиків
- `requirements.txt` - залежності проєкту

## Створення віртуального середовища

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Запуск файлів

```bash
python task1_singly_linked_list.py
python task2_pythagoras_tree.py
python task3_dijkstra_heap.py
python task4_heap_visualization.py
python task5_tree_traversal_visualization.py
python task6_food_knapsack.py
python task7_monte_carlo_dice.py
```

## Висновки до завдання 7

Метод Монте-Карло показує результати, близькі до аналітичних імовірностей, якщо виконати велику кількість симуляцій.

Найчастіше випадає сума 7, оскільки вона має найбільшу кількість можливих комбінацій.

Суми 2 і 12 трапляються найрідше, бо для кожної з них існує лише одна комбінація.

Чим більша кількість експериментів, тим ближчі результати моделювання до теоретичних значень.