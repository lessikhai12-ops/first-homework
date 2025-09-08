# Стандартний час тренування
default_time = 60


def training_session(rounds):
    """Зменшує час кожного раунду на 5 хв."""
    time_per_round = default_time

    def adjust_time():
        nonlocal time_per_round

        for i in range(1, rounds + 1):
            time_per_round = time_per_round - 5
            print(f"Раунд {i}: {time_per_round}хв")
    adjust_time()


training_session(5)