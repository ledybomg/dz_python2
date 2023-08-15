def find_indices_in_range(lst, min_val, max_val):
    indices = []
    for i, num in enumerate(lst):
        if min_val <= num <= max_val:
            indices.append(i)
    return indices

length = int(input("Введите длину списка: "))
user_list = []

for i in range(length):
    num = int(input(f"Введите значение элемента {i + 1}: "))
    user_list.append(num)

print("Введенный список:", user_list)

min_range = int(input("Введите минимальное значение диапазона поиска: "))
max_range = int(input("Введите максимальное значение диапазона поиска: "))

indices = find_indices_in_range(user_list, min_range, max_range)
print("Индексы элементов в заданном диапазоне:", indices)
