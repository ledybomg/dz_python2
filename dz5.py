print("Пожалуйста, введите кол-во элементов множества n:")
n = input()
print("Пожалуйста, введите кол-во элементов множества m:")
n_int = int(n)
m = input()
m_int = int(m)
print("Пожалуйста, введите элементы множества n:")

while True:
    n_items_list = input().split(' ')
    if len(n_items_list) != n_int:
        print("Количество элементов множества n не сходится! Пожалуйста, введите правильное количество элементов:")
    else:
        break

print("Пожалуйста, введите элементы множества m:")
while True:
    m_items_list = input().split(' ')
    if len(m_items_list) != m_int:
        print("Количество элементов множества m не сходится! Пожалуйста, введите правильное количество элементов:")
    else:
        break

set_n_items = set(n_items_list)
set_m_items = set(m_items_list)
nm_set = list(set(set_n_items & set_m_items)).sort()
if nm_set is not None:
    print("Ваш результат:", nm_set)
else:
    print("В множествах нет повторяющихся элементов!")




