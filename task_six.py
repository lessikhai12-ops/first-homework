def create_calculator(operator):
    """Створює функцію для виконання операцій заданого оператора"""
    def calculate(a, b):
        if operator == '+':
            return f"{a} + {b} = {a + b}"

        elif operator == '-':
            return f"{a} - {b} = {a - b}"

        elif operator == '*':
            return f"{a} * {b} = {a * b}"

        elif operator == '/':
            if b != 0:
                return f"{a}/{b} = {a / b:.2f}"
            else:
                return f"{a}/{b} = Не визначено"
        else:
            return "Невідомий оператор"
    return calculate

#Створює функції для обчислень
add = create_calculator('+')
sub = create_calculator('-')
mul = create_calculator('*')
div = create_calculator('/')

#Тестування
print(add(17, 56))
print(sub(33, 34))
print(mul(7, 0))
print(div(3, 0))
print(div(23, 6))