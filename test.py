import random
list = [0,0,0,0,0,0,0,0,0,0]
i = random.randint(1,9)
print(i)
if list[i] == 0:
    list[i] = i
print (list)
