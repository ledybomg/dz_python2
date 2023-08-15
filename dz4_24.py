def find_max_blackberries(hedge):
    sum_arr = []
    for i in hedge.keys():
        if i == 1:
            sum_arr.append(len(hedge.keys()) + hedge[i] + hedge[i + 1])
        elif i == len(hedge.keys()):
            sum_arr.append(hedge[i - 1] + hedge[i] + hedge[1])
        else:
            sum_arr.append(hedge[i - 1] + hedge[i] + hedge[i + 1])
    return max(sum_arr)


input_data = {
    1: 2,
    2: 4,
    3: 10,
    4: 1,
    5: 23
}

print(find_max_blackberries(input_data))




