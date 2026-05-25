import math
import matplotlib.pyplot as plt


def draw_branch(x, y, length, angle, level, ax):
    if level == 0:
        return

    x2 = x + length * math.cos(math.radians(angle))
    y2 = y + length * math.sin(math.radians(angle))

    ax.plot([x, x2], [y, y2], color="green", linewidth=level)

    draw_branch(x2, y2, length * 0.7, angle + 45, level - 1, ax)
    draw_branch(x2, y2, length * 0.7, angle - 45, level - 1, ax)


def main():
    level = int(input("Введіть рівень рекурсії: "))

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_title("Фрактал 'Дерево Піфагора'")
    ax.set_aspect("equal")
    ax.axis("off")

    draw_branch(0, 0, 100, 90, level, ax)

    plt.show()


if __name__ == "__main__":
    main()