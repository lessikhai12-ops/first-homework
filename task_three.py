# Глобальна знижка
discount = 0.1


def create_order(price, is_vip=False):
    """Створює замовлення з урахуванням глобальної та додаткової знижки."""
    new_price = price * (1 - discount)

    def apply_additional_discount(additional_discount):
        nonlocal new_price
        new_price = price * (1 - discount - additional_discount)

    # Якщо клієнт VIP, додаємо додаткову знижку
    if is_vip:
        apply_additional_discount(0.2)

    print(f"Фінальна ціна: {new_price:.2f} грн")


# Тестування
create_order(1000)  # товар коштує 1000 грн
create_order(1000, is_vip = True)


