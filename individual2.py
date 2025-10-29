a = int(input("Введите число a: "))
b = int(input("Введитве число b: "))

result = 1 * ((a % b == 0) or (b % a == 0))

print(result)