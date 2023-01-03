import re


def numeric(temp):
    temp += " "
    number = ""
    list_of_numbers = []
    for i in range(len(temp)):
        if temp[i] in numbers:
            number += temp[i]
        else:
            if number != "":
                list_of_numbers.append(number)
            number = ""
    return list_of_numbers


def PrintPasTriangle(rows):
    row = [1]
    for i in range(rows):
        row = [sum(x) for x in zip([0] + row, row + [0])]
    return row


if __name__ == '__main__':
    numbers = "0123456789"
    string = "(-52m+343)^4"
    start = string.find("(")
    end = string.find(")")
    temple = string[start + 1:end]
    print(string[start + 1:end])

    #answer=numeric(temple)





    first = "a"
    second = "b"
    power = 4
    triangle = PrintPasTriangle(power)
    otvet = ""
    for i in range(len(triangle)):
        otvet+=str(triangle[i])+first+"^"+str(power-i)+second+"^"+str(i)+"+"

    print(otvet)

