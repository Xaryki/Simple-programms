def pascal(n):
    lst = []
    for i in range(n + 1):
        lst.append([1] + [0] * n)
    """Заполнение списка числами путем сложения двух соседних элементов """
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            lst[i][j] = lst[i - 1][j] + lst[i - 1][j - 1]
    return lst[n]


if __name__ == "__main__":
    print(pascal(5))
