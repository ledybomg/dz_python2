a1 = int(input("Введите первый элемент прогрессии (a1): "))
d = int(input("Введите разность прогрессии (d): "))
n = int(input("Введите количество элементов (n): "))

progression = []

for i in range(n):
    an = a1 + i * d
    progression.append(an)

print("Полученная арифметическая прогрессия:")
for num in progression:
    print(num)