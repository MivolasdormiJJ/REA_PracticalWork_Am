def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b
print("Умножение:", multiply(5, 3))
print("Деление:", divide(10, 2))