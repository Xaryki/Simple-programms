def Snail_sort(snail_map):
    a = []
    while snail_map:
        a.extend(snail_map.pop(0))
        snail_map = list(zip(*snail_map))  # Транспонирование
        snail_map.reverse()  # переворот
    return a


if __name__ == '__main__':
    array = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    #print(Snail_sort(array))
for row in array:
    print(*row)