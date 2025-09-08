subscribers = []


def subscribe(name):
     subscribers.append(name)


     def confirm_subsription():
        print("Підписка підтверджена для", name)
     confirm_subsription()

def unsubscribe(name):
    if name in subscribers:
        subscribers.remove(name)
        print("Користувача", name, "успішно відписано")

    else:
        print("Користувача", name, "не знайдено серед підписників")


subscribe("Ігор")
subscribe("Аліна")
subscribe("Соня")
subscribe("Світлана")
unsubscribe("Ігор")
unsubscribe("Світлана")
unsubscribe("Катерина")



