def powers_of_two(N):
    k = 0
    while 2 ** k <= N:
        print(2 ** k)
        k += 1

N = int(input("Введите число N: "))
powers_of_two(N)
