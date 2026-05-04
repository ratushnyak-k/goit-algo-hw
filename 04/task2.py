import math


def koch_curve(p1, p5, order):
    """
    Рекурсивно будує одну сторону кривої Коха між двома точками.

    p1, p5  - початкова та кінцева точки відрізка.
    order   - рівень рекурсії.
    """
    # Базовий випадок рекурсії:
    # якщо рівень рекурсії дорівнює 0, просто повертаємо відрізок
    if order == 0:
        return [p1, p5]

    # Розпаковуємо координати початкової та кінцевої точок
    x1, y1 = p1
    x5, y5 = p5

    # Обчислюємо прирости по x та y для 1/3 відрізка
    dx = (x5 - x1) / 3
    dy = (y5 - y1) / 3

    # Точка p2 - кінець першої третини відрізка
    p2 = (x1 + dx, y1 + dy)

    # Точка p4 - кінець другої третини відрізка
    p4 = (x1 + 2 * dx, y1 + 2 * dy)

    # Вектор від p2 до p4
    vx = p4[0] - p2[0]
    vy = p4[1] - p2[1]

    # Повертаємо вектор на -60 градусів,
    # щоб отримати вершину "зубця" p3
    angle = -math.pi / 3
    p3 = (
        p2[0] + vx * math.cos(angle) - vy * math.sin(angle),
        p2[1] + vx * math.sin(angle) + vy * math.cos(angle),
    )

    # Рекурсивно будуємо 4 частини кривої Коха:
    # p1 -> p2, p2 -> p3, p3 -> p4, p4 -> p5
    part1 = koch_curve(p1, p2, order - 1)
    part2 = koch_curve(p2, p3, order - 1)
    part3 = koch_curve(p3, p4, order - 1)
    part4 = koch_curve(p4, p5, order - 1)

    # Об'єднуємо всі частини в один список точок.
    # Щоб уникнути дублювання точок на стиках, відкидаємо останню точку
    # у перших трьох частинах.
    return part1[:-1] + part2[:-1] + part3[:-1] + part4


def save_svg(points, filename="koch_snowflake.svg"):
    """
    Зберігає список точок у SVG-файл.
    Це дозволяє візуалізувати фрактал без додаткових бібліотек.
    """
    # Знаходимо межі фігури
    min_x = min(x for x, y in points)
    max_x = max(x for x, y in points)
    min_y = min(y for x, y in points)
    max_y = max(y for x, y in points)

    # Додаємо відступи від країв зображення
    padding = 20
    width = max_x - min_x + 2 * padding
    height = max_y - min_y + 2 * padding

    # Перетворюємо математичні координати в координати SVG
    svg_points = []
    for x, y in points:
        sx = x - min_x + padding
        sy = y - min_y + padding
        svg_points.append(f"{sx},{sy}")

    # Формуємо рядок точок для polyline
    polyline = " ".join(svg_points)

    # Створюємо SVG-код
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" fill="white"/>
  <polyline points="{polyline}" fill="none" stroke="blue" stroke-width="1"/>
</svg>"""

    # Записуємо SVG у файл
    with open(filename, "w", encoding="utf-8") as file:
        file.write(svg)


def draw_koch_snowflake(order):
    """
    Будує повну сніжинку Коха з трьох сторін рівностороннього трикутника.
    """
    # Задаємо розмір трикутника
    size = 600
    height = size * math.sqrt(3) / 2

    # Визначаємо вершини рівностороннього трикутника
    a = (0, height)
    b = (size / 2, 0)
    c = (size, height)

    # Будуємо 3 сторони сніжинки Коха
    side1 = koch_curve(a, b, order)
    side2 = koch_curve(b, c, order)
    side3 = koch_curve(c, a, order)

    # Об'єднуємо точки всіх сторін у єдиний контур
    points = side1[:-1] + side2[:-1] + side3

    save_svg(points)

    print("Фрактал збережено у файл koch_snowflake.svg")


def main():
    """
    Основна функція програми:
    запитує рівень рекурсії та запускає побудову фрактала.
    """
    try:
        level = int(input("Введіть рівень рекурсії: "))

        if level < 0:
            print("Рівень рекурсії має бути невід’ємним числом.")
            return

        draw_koch_snowflake(level)

    except ValueError:
        print("Будь ласка, введіть ціле число.")

if __name__ == "__main__":
    main()