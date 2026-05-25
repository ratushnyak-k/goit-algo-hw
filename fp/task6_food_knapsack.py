items = {
    "pizza":     {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog":   {"cost": 30, "calories": 200},
    "pepsi":     {"cost": 10, "calories": 100},
    "cola":      {"cost": 15, "calories": 220},
    "potato":    {"cost": 25, "calories": 350},
}


def greedy_algorithm(budget: int, items: dict) -> tuple[list, int, int]:
    """
    Жадібний алгоритм: вибирає страви за спаданням відношення calories/cost,
    поки вистачає бюджету.
    Повертає (список страв, загальна вартість, загальна калорійність).
    """
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True,
    )
    chosen = []
    total_cost = 0
    total_calories = 0

    for name, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            chosen.append(name)
            total_cost += info["cost"]
            total_calories += info["calories"]

    return chosen, total_cost, total_calories


def dynamic_programming(budget: int, items: dict) -> tuple[list, int, int]:
    """
    Динамічне програмування (0/1 knapsack).
    'Вага' = вартість страви, 'цінність' = калорії.
    Повертає (список страв, загальна вартість, загальна калорійність).
    """
    names = list(items.keys())
    costs = [items[n]["cost"] for n in names]
    cals = [items[n]["calories"] for n in names]
    n = len(names)

    # dp[i][w] = максимальні калорії для перших i страв при бюджеті w
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            dp[i][w] = dp[i - 1][w]
            if costs[i - 1] <= w:
                take = dp[i - 1][w - costs[i - 1]] + cals[i - 1]
                if take > dp[i][w]:
                    dp[i][w] = take

    # Відновлення вибраних страв
    chosen = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(names[i - 1])
            w -= costs[i - 1]

    total_cost = sum(items[name]["cost"] for name in chosen)
    total_calories = sum(items[name]["calories"] for name in chosen)

    return chosen, total_cost, total_calories


if __name__ == "__main__":
    budget = 100

    print(f"Бюджет: {budget} грн\n")

    greedy_chosen, greedy_cost, greedy_cal = greedy_algorithm(budget, items)
    print("=== Жадібний алгоритм ===")
    print(f"Страви:      {greedy_chosen}")
    print(f"Вартість:    {greedy_cost} грн")
    print(f"Калорійність:{greedy_cal} ккал")

    print()

    dp_chosen, dp_cost, dp_cal = dynamic_programming(budget, items)
    print("=== Динамічне програмування ===")
    print(f"Страви:      {dp_chosen}")
    print(f"Вартість:    {dp_cost} грн")
    print(f"Калорійність:{dp_cal} ккал")