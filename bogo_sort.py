
import random
import sys


def is_sorted(list):
    for index in range(len(list) -1):
        if list[index] > list[index +1]:
            return False
    return True

def bogo_sort(list):
    attemps = 0
    while not is_sorted(list):
        random.shuffle(list)
        attemps += 1
    print(attemps)    
    return list

list = [33, 5, 345,8, 10]

print(bogo_sort(list))
        
        