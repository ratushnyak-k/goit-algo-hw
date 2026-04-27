import queue
import random

def generate_request(request_queue):
    """Генерує нову заявку і додає її до черги."""
    request_id = random.randint(1000, 9999)
    request_queue.put(request_id)
    print(f"Нову заявку #{request_id} додано до черги.")

def process_request(request_queue):
    """Обробляє заявку з черги (видаляє і 'опрацьовує')."""
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Заявку #{request_id} обробляється...")
    else:
        print("Черга порожня. Немає заявок для обробки.")

def main():
    request_queue = queue.Queue()

    print("=== Симуляція сервісного центру ===")
    print("Команди: 'add' — додати заявку, 'process' — обробити, 'quit' — вийти\n")

    while True:
        command = input("Введіть команду: ").strip().lower()
        if command == "add":
            generate_request(request_queue)
        elif command == "process":
            process_request(request_queue)
        elif command == "quit":
            print("Завершення роботи.")
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()