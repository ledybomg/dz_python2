def min_flips(coins):
    heads = coins.count('H')
    tails = len(coins) - heads
    return min(heads, tails)

n = int(input("Введите общее количество монеток: "))
coins = input("Введите строку, представляющую расположение монеток ('H' - решка, 'T' - герб): ").upper()

if len(coins) != n:
    print("Некорректный ввод строки.")
else:
    result = min_flips(coins)
    print(f"Минимальное количество монеток, которые нужно перевернуть: {result}")
