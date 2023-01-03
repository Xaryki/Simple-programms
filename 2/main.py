def fibonacci(signature, n):
    res = signature[:n]
    for i in range(n-2):
        res.append(sum(map(int,res[i:])))
    return res


if __name__ == '__main__':
    print(fibonacci([139, 53, 2], 5))
