from random import randint as rd
my_set = set()
k = 5
temp = set()
while len(my_set) != 25:
    temp.add(rd(1, 75))
    if len(my_set) % k == 0 and len(my_set) != 0 :
        my_set.add()
my_set = list(my_set)
my_set[12] = 0
