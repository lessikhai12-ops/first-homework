#Глобальна змінна
total_expense = 0


def add_expense(new_expense):
    """Додає витрату до загальної суми."""
    global total_expense
    total_expense += new_expense


def get_expense():
    """Повертає загальну суму витрат"""
    return total_expense


def main():
    """Простий консольний інтерфейс для трекінгу витрат."""
    while True:
        print("\nМеню:")
        print("1. Додати витрату")
        print("2. Переглянути загальну суму")
        print("3. Вихід")
        choice = input("Оберіть опцію: ")

        if choice == "1":
            try:
                amount = float(input("Введіть суму витрат: "))
                add_expense(amount)
                print(f"Витрату {amount:.2f} грн додано.")
            except ValueError:
                print("Помилка: введіть число.")
        elif choice == "2":
            print(f"Загальна сума витрат: {get_expense():.2f} грн")
        elif choice == "3":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Запуск програми
main()



