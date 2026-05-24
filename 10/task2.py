import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi


def f(x):
    return x ** 2


def monte_carlo_integral(func, a: float, b: float, n_points: int) -> float:
    """
    Метод Монте-Карло для обчислення визначеного інтеграла.
    Генерує n_points випадкових точок на [a, b],
    рахує середнє значення f(x) і множить на довжину відрізка.
    """
    x_random = np.random.uniform(a, b, n_points)
    return (b - a) * np.mean(func(x_random))


def plot_function(func, a: float, b: float) -> None:
    """Побудова графіка функції із зафарбованою областю інтегрування."""
    x = np.linspace(a - 0.5, b + 0.5, 400)
    y = func(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, "r", linewidth=2, label="f(x) = x²")

    ix = np.linspace(a, b)
    iy = func(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3, label="Область інтегрування")

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title(f"Графік інтегрування f(x) = x² від {a} до {b}")
    ax.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    a, b = 0, 2

    plot_function(f, a, b)

    analytical = (b ** 3 - a ** 3) / 3
    print("=" * 55)
    print(f"{'Аналітичний результат':<35}: {analytical:.6f}")

    quad_result, quad_error = spi.quad(f, a, b)
    print(f"{'quad (SciPy)':<35}: {quad_result:.6f}  (похибка: {quad_error:.2e})")

    print(f"{'Метод Монте-Карло':<35}   {'Результат':>10}   {'Відхилення':>12}")
    print("-" * 62)
    for n in [100, 1_000, 10_000, 100_000, 1_000_000]:
        mc_result = monte_carlo_integral(f, a, b, n)
        diff = abs(mc_result - analytical)
        print(f"  n = {n:<12,}              {mc_result:>10.6f}   {diff:>12.6f}")

    print("=" * 55)
    print("\nВисновок: зі збільшенням кількості точок n")
    print("точність методу Монте-Карло зростає.")
    print(f"Аналітичне значення: {analytical:.6f}")
    print(f"quad:                {quad_result:.6f}")