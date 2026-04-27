from collections import deque

def is_palindrome(s: str) -> bool:
    """
    Перевіряє, чи є рядок паліндромом.
    Нечутливо до регістру та пробілів.
    """
    cleaned = s.replace(" ", "").lower()
    char_deque = deque(cleaned)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

def main():
    test_strings = [
        "racecar",
        "Hello",
        "A man a plan a canal Panama",
        "Never odd or even",
        "Python",
        "madam",
        "",
    ]

    print("=== Перевірка паліндромів ===\n")
    for s in test_strings:
        result = is_palindrome(s)
        print(f"'{s}' -> {'Паліндром' if result else 'Не паліндром'}")

    print("\n--- Введіть власний рядок ---")
    while True:
        user_input = input("Рядок (або 'quit' для виходу): ").strip()
        if user_input.lower() == "quit":
            break
        result = is_palindrome(user_input)
        print(f"'{user_input}' -> {'Паліндром' if result else 'Не паліндром'}")

if __name__ == "__main__":
    main()