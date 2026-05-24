import time

COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount: int) -> dict:
    """
    Жадібний алгоритм: спочатку вибирає найбільший доступний номінал.
    Повертає словник {номінал: кількість}.
    """
    result = {}
    for coin in COINS:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result


def find_min_coins(amount: int) -> dict:
    """
    Динамічне програмування: знаходить мінімальну кількість монет.
    Повертає словник {номінал: кількість}.
    """
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in COINS:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    result = {}
    current = amount
    while current > 0:
        coin = last_coin[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result


def benchmark(amount: int, runs: int = 1000) -> None:
    """Порівнює час виконання двох алгоритмів."""
    start = time.perf_counter()
    for _ in range(runs):
        find_coins_greedy(amount)
    greedy_time = time.perf_counter() - start

    start = time.perf_counter()
    for _ in range(runs):
        find_min_coins(amount)
    dp_time = time.perf_counter() - start

    print(f"\nПорівняння для суми {amount} ({runs} запусків):")
    print(f"  Жадібний алгоритм : {greedy_time:.6f} с")
    print(f"  Динамічне прогр.  : {dp_time:.6f} с")
    print(f"  DP повільніший у  : {dp_time / greedy_time:.1f} разів")


if __name__ == "__main__":
    test_amounts = [113, 85, 37, 999]

    print("=" * 50)
    print("Жадібний алгоритм (find_coins_greedy):")
    print("=" * 50)
    for amount in test_amounts:
        result = find_coins_greedy(amount)
        total = sum(k * v for k, v in result.items())
        print(f"  Сума {amount:>4}: {result}  | перевірка: {total}")

    print()
    print("=" * 50)
    print("Динамічне програмування (find_min_coins):")
    print("=" * 50)
    for amount in test_amounts:
        result = find_min_coins(amount)
        total = sum(k * v for k, v in result.items())
        print(f"  Сума {amount:>4}: {result}  | перевірка: {total}")

    benchmark(113)
    benchmark(9999)