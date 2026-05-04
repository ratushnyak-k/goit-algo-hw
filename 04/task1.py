import argparse
import shutil
from pathlib import Path


def copy_and_sort_files(source_dir: Path, dest_dir: Path) -> None:
    """
    Рекурсивно проходить по всіх файлах і папках у source_dir,
    копіює файли до dest_dir та сортує їх у підпапки за розширенням.
    """
    try:
        for item in source_dir.iterdir():
            if item.is_dir():
                copy_and_sort_files(item, dest_dir)
            elif item.is_file():
                extension = item.suffix[1:] if item.suffix else "no_extension"
                target_folder = dest_dir / extension
                target_folder.mkdir(parents=True, exist_ok=True)

                target_file = target_folder / item.name
                shutil.copy2(item, target_file)
                print(f"Файл {item} скопійовано до {target_file}")

    except Exception as e:
        print(f"Помилка при обробці директорії {source_dir}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Рекурсивне копіювання та сортування файлів за розширенням"
    )
    parser.add_argument("source", help="Шлях до вихідної директорії")
    parser.add_argument(
        "destination",
        nargs="?",
        default="dist",
        help="Шлях до директорії призначення (за замовчуванням: dist)"
    )

    args = parser.parse_args()

    source_path = Path(args.source)
    destination_path = Path(args.destination)

    if not source_path.exists() or not source_path.is_dir():
        print("Помилка: вихідна директорія не існує або це не директорія.")
        return

    destination_path.mkdir(parents=True, exist_ok=True)

    copy_and_sort_files(source_path, destination_path)
    print("Сортування файлів завершено.")


if __name__ == "__main__":
    main()