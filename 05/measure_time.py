import timeit
from boyer_moore import boyer_moore_search
from kmp import kmp_search
from rabin_karp import rabin_karp_search


def read_file(path):
    encodings = ["utf-8", "utf-8-sig", "cp1251", "latin-1"]
    for enc in encodings:
        try:
            with open(path, "r", encoding=enc) as f:
                return f.read()
        except (UnicodeDecodeError, LookupError):
            continue
    raise ValueError(f"Не вдалося прочитати файл: {path}")


def measure(func, text, pattern, repeats=10):
    return timeit.timeit(lambda: func(text, pattern), number=repeats)


article1 = read_file("article1.txt")
article2 = read_file("article2.txt")

# Підрядки для статті 1 — замін на ті, що реально є в тексті
existing_1 = "алгоритм"
fictional_1 = "неіснуючий_рядок_xyz_99999"

# Підрядки для статті 2 — замін на ті, що реально є в тексті
existing_2 = "структура даних"
fictional_2 = "вигаданий_підрядок_abc_88888"

algorithms = {
    "Boyer-Moore": boyer_moore_search,
    "KMP":         kmp_search,
    "Rabin-Karp":  rabin_karp_search,
}

tests = [
    ("Article 1", article1, existing_1,  "existing"),
    ("Article 1", article1, fictional_1, "fictional"),
    ("Article 2", article2, existing_2,  "existing"),
    ("Article 2", article2, fictional_2, "fictional"),
]

print(f"{'Article':<12} {'Type':<10} {'Algorithm':<14} {'Time (sec)':>12}")
print("-" * 52)

results = {}

for article_name, text, pattern, ptype in tests:
    for algo_name, algo_func in algorithms.items():
        t = measure(algo_func, text, pattern)
        results[(article_name, ptype, algo_name)] = t
        print(f"{article_name:<12} {ptype:<10} {algo_name:<14} {t:>12.6f}")

print("\n--- Найшвидший алгоритм ---")
for article in ["Article 1", "Article 2"]:
    for ptype in ["existing", "fictional"]:
        subset = {k: v for k, v in results.items() if k[0] == article and k[1] == ptype}
        best = min(subset, key=subset.get)
        print(f"{article} / {ptype}: {best[2]} ({subset[best]:.6f} sec)")