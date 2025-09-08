# Глобальний список для зберігання подій
events = []


def event_calendar():
    """Створює календар подій із функціями додавання, видалення та перегляду."""
    def add_event(event):
        events.append(event)
        print(f"Подію '{event}' додано.")

    def remove_event(event):
        if event in events:
            events.remove(event)
            print(f"Подію '{event}' видалено.")
        else:
            print(f"Подію '{event}' не знайдено.")

    def show_events():
        if events:
            print("Майбутні події:")
            for i, e in enumerate(events, start=1):
                print(f"{i}. {e}")
        else:
            print("Немає запланованих подій.")

    return add_event, remove_event, show_events


# Використання
add, remove, show = event_calendar()

add("День народження")
add("Зустріч із друзями")
show()

remove("День народження")
show()
