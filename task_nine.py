def memoize(func):
    """Функція-декоратор для кешування результатів."""
    cache = {}

    def wrapper(n):
        if n in cache:
            print(f"Беремо з кешу: {n}")
            return cache[n]
        print(f"Обчислюємо: {n}")
        result = func(n)
        cache[n] = result
        return result

    return wrapper


# Приклад: обчислення чисел Фібоначчі
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Приклад: факторіал
@memoize
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Тест
print("Фібоначчі:")
print(fibonacci(10))

print("\nФакторіал:")
print(factorial(6))
