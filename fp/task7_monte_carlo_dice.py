import random
import matplotlib.pyplot as plt


THEORETICAL = {
    2:  1/36,
    3:  2/36,
    4:  3/36,
    5:  4/36,
    6:  5/36,
    7:  6/36,
    8:  5/36,
    9:  4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36,
}


def simulate_dice(num_rolls: int = 1_000_000) -> dict:
    """
    Імітує num_rolls кидків двох кубиків.
    Повертає словник {сума: кількість випадань}.
    """
    counts = {s: 0 for s in range(2, 13)}
    for _ in range(num_rolls):
        roll = random.randint(1, 6) + random.randint(1, 6)
        counts[roll] += 1
    return counts


def compute_probabilities(counts: dict) -> dict:
    total = sum(counts.values())
    return {s: c / total for s, c in counts.items()}


def print_table(probabilities: dict):
    print(f"{'Сума':>5} | {'Монте-Карло':>12} | {'Теорія':>10} | {'Різниця':>10}")
    print("-" * 48)
    for s in range(2, 13):
        mc = probabilities[s]
        th = THEORETICAL[s]
        diff = abs(mc - th)
        print(f"{s:>5} | {mc:>11.4%} | {th:>9.4%} | {diff:>9.4%}")


def plot_results(probabilities: dict):
    sums = list(range(2, 13))
    mc_probs = [probabilities[s] * 100 for s in sums]
    th_probs = [THEORETICAL[s] * 100 for s in sums]

    x = range(len(sums))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    bars1 = ax.bar([i - width / 2 for i in x], mc_probs, width,
                   label="Монте-Карло", color="steelblue")
    bars2 = ax.bar([i + width / 2 for i in x], th_probs, width,
                   label="Теорія", color="orange", alpha=0.8)

    ax.set_xlabel("Сума двох кубиків")
    ax.set_ylabel("Імовірність (%)")
    ax.set_title("Метод Монте-Карло vs Теоретичні ймовірності")
    ax.set_xticks(list(x))
    ax.set_xticklabels(sums)
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    NUM_ROLLS = 1_000_000
    print(f"Симуляція {NUM_ROLLS:,} кидків двох кубиків...\n")

    counts = simulate_dice(NUM_ROLLS)
    probs = compute_probabilities(counts)

    print_table(probs)
    plot_results(probs)