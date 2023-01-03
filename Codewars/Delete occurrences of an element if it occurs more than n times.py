from collections import Counter

"""#1"""


def delete_nth(array, N):
    array = array[::-1]
    cnt = Counter(array)
    for number in cnt:
        if cnt[number] > N:
            for i in range(cnt[number] - N):
                array.remove(number)
    return array[::-1]


"""#2"""


def delete_nth2(array, N):
    answer = []
    for number in array:
        if answer.count(number) < N:
            answer.append(number)
    return answer


if __name__ == '__main__':
    array = [20, 37, 20, 21]
    N = 1
    print(delete_nth(array, N))
    print(delete_nth2(array, N))
