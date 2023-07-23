def find_numbers(S, P):
    for X in range(1, 1001):
        Y = S - X
        if 1 <= Y <= 1000 and X * Y == P:
            return X, Y
    return None, None

S = int(input("Введите сумму чисел (S): "))
P = int(input("Введите произведение чисел (P): "))

X, Y = find_numbers(S, P)

if X is not None and Y is not None:
    print(f"Задуманные числа: {X} и {Y}")
else:
    print("Невозможно определить числа по заданным значениям S и P.")
