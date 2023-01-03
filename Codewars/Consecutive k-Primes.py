"""#1"""

def consec_kprimes(k, arr):
    answer=0
    an=[]
    for number in arr:
        ans = []
        delitel=2

        while number != 1:
            if number % delitel == 0:
                ans.append(delitel)
                number=number/delitel
                delitel=2
                continue
            delitel += 1
        an.append(len(ans))
        print(ans)
    for i in range(len(an)-1):
        if ( an[i] == an[i+1] ) and an[i] == k:
            answer+=1
    return answer


if __name__ == '__main__':
    arr=[10158, 10182, 10184, 10172, 10179, 10168, 10156, 10165, 10155, 10161, 10178, 10170]
    arr2 = [10005, 10030, 10026, 10008, 10016, 10028, 10004]
    print(consec_kprimes(4,arr2))