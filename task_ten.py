def create_product(name):
    """Функція для створення товару (карирування + замикання)."""

    def set_price(price):
        def set_quantity(quantity):
            product = {
                "name": name,
                "price": price,
                "quantity": quantity,
            }

            def update_price(new_price):
                nonlocal product
                product["price"] = new_price
                return f"Ціну товару '{product['name']}' змінено на {new_price} грн"

            # додаємо функцію в словник
            product["update_price"] = update_price
            return product

        return set_quantity

    return set_price


# Тест
laptop = create_product("Ноутбук")(20000)(5)

print(laptop)


print(laptop )

print(laptop)
