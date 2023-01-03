"""Типа пузырек"""
def move_zeros(lst):
    for j in range(len(lst)):
        for i in range(len(lst) - 1):
            if lst[i] == 0:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

"""Норм решение"""
def move_zeros2(lst):
    for number in lst:
        if number == 0:
            lst.remove(number)
            lst.append(number)
    return lst

if __name__ == '__main__':
    lst = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
    print(move_zeros(lst))
    print(move_zeros2(lst))