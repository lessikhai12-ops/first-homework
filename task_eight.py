def create_user_settings():
    """Створює систему зберігання налаштувань користувача за допомогою замикання."""
    settings_data = {
        "theme": "light",
        "language": "ua",
        "notifications": True,
    }

    def settings(action, key=None, value=None):
        nonlocal settings_data

        if action == "get":
            if key:
                return settings_data.get(key, "Налаштування не знайдено")
            return settings_data

        elif action == "set" and key:
            settings_data[key] = value
            return f"Налаштування '{key}' змінено на {value}"

        elif action == "delete" and key:
            if key in settings_data:
                del settings_data[key]
                return f"Налаштування '{key}' видалено"
            return "Такого налаштування немає"

        else:
            return "Невідома дія"

    return settings


# --- Тест ---
user_settings = create_user_settings()

print(user_settings("get"))
print(user_settings("get", "theme"))
print(user_settings("set", "theme", "dark"))
print(user_settings("get", "theme"))
print(user_settings("set", "language", "en"))
print(user_settings("delete", "notifications"))
print(user_settings("get"))
