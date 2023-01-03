lst = "anton"
answer = ""
for j in range(int(input())):
    text = str(input())
    n = 0
    while text.find(lst[n]) != -1:
        text = text[text.find(lst[n])+1:]
        n += 1
        if n == 5:
            answer += str(j+1) + " "
            n = 0
            break
print(answer)

