def ips_between(start, end):
    calc = lambda n, m: (int(end.split(".")[n]) - int(start.split(".")[n])) * m
    return calc(0, 256 * 256 * 256) + calc(1, 256 * 256) + calc(2, 256) + calc(3, 1)


def ips_between2(start, end):
    starts = list(map(int, start.split(".")))
    ends = list(map(int, end.split(".")))
    list_multiplication = [256*256*256, 256*256, 256, 1]
    temp = 0
    for i in range(len(starts)):
        temp += (ends[i]-starts[i])*list_multiplication[i]
    return temp


if __name__ == "__main__":
    print(ips_between2("74.222.110.119", "75.96.187.119"))
