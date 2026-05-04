import argparse
import shutil
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(
        description="Рекурсивне копіювання та сортування файлів за розширенням"
    )
    parser.add_argument("source", type=Path, help="Шлях до вихідної директорії")
    parser.add_argument(
        "destination",
        nargs="?",
        default="dist",
        type=Path,
        help="Шлях до директорії призначення (за замовчуванням: dist)",
    )
    return parser.parse_args()


def copy_directory(source_dir: Path, destination_dir: Path):
    try:
        for item in source_dir.iterdir():
            if item.is_dir():
                # Рекурсивний виклик
                copy_directory(item, destination_dir) 
            elif item.is_file():
                try:
                    # Отримуємо розширення (без крапки)
                    extension = item.suffix[1:] if item.suffix else "no_extension"

                    # Створюємо піддиректорію
                    target_dir = destination_dir / extension
                    target_dir.mkdir(parents=True, exist_ok=True)

                    # Формуємо шлях до нового файлу
                    counter = 1
                    target_file = target_dir / item.name

                    while target_file.exists():
                        target_file = target_dir / f"{item.stem}_{counter}{item.suffix}"
                        counter += 1
                    # target_file = target_dir / item.name

                    # Копіюємо файл
                    shutil.copy(item, target_file)

                except Exception as error:
                    print(f"Помилка обробки файлу {item}: {error}")

    except Exception as error:
        print(f"Помилка доступу до директорії {source_dir}: {error}")


def main():
    args = parse_args()

    source_path = args.source
    destination_path = args.destination

    # Перевірка вихідної директорії
    if not source_path.exists() or not source_path.is_dir():
        print("Помилка: вихідна директорія не існує або не є директорією.")
        return

    try:
        # Створюємо директорію призначення
        destination_path.mkdir(parents=True, exist_ok=True)

        # Запуск рекурсивної обробки
        copy_directory(source_path, destination_path)

        print("Всі файли успішно скопійовані та відсортовані.")

    except Exception as error:
        print(f"Помилка: {error}")


if __name__ == "__main__":
    main()