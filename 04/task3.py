import random
import timeit


def insertion_sort(arr):
    """
    Сортування вставками.
    """
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge_sort(arr):
    """
    Сортування злиттям.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """
    Злиття двох відсортованих списків.
    """
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def timsort(arr):
    """
    Використання вбудованого Timsort.
    """
    return sorted(arr)


def measure_time(sort_function, data, repeat=5):
    """
    Вимірює середній час виконання сортування.
    """
    stmt = lambda: sort_function(data)
    total_time = timeit.timeit(stmt, number=repeat)
    return total_time / repeat


def main():
    sizes = [100, 1000, 5000]
    data_sets = {
        "Випадковий масив": lambda size: [random.randint(0, 10000) for _ in range(size)],
        "Відсортований масив": lambda size: list(range(size)),
        "Майже відсортований масив": lambda size: list(range(size - 1)) + [0],
        "Масив у зворотному порядку": lambda size: list(range(size, 0, -1)),
    }

    for size in sizes:
        print(f"\n--- Розмір масиву: {size} ---")

        for data_name, data_generator in data_sets.items():
            data = data_generator(size)
            print(f"\n{data_name}:")

            insertion_time = measure_time(insertion_sort, data)
            merge_time = measure_time(merge_sort, data)
            timsort_time = measure_time(timsort, data)

            print(f"Сортування вставками: {insertion_time:.6f} сек")
            print(f"Сортування злиттям:   {merge_time:.6f} сек")
            print(f"Timsort:              {timsort_time:.6f} сек")


if __name__ == "__main__":
    main()