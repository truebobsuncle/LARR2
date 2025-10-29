import math
print("Введите катеты прямоугольного треугольникаа:")
a = float(input("Первый катет: "))
b = float(input("Второй катет: "))
c = math.sqrt(a**2 + b**2)
perimeter = a + b + c
print(f"Гипотенуза: {c:.2f}")
print(f"Периметр треугольника: {perimeter:.2f}")