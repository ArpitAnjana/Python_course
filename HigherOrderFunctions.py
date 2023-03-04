# ======higher order function========

import numbers
from unittest import result

from numpy import full, number

# easy method pro
def double_number(number:int)->int:
    return number*2

# print(double_number(1))
print(list(map(double_number,[1,2,3,4])))

# difficult method beginner
def double_number2(numbers:int)->int:
    result=[]
    for number in numbers:
        result.append(number*2)
    return result

print(double_number2([1,2,3]))

# more pro level using lambda and map

print(set(map(lambda double: double*2, [1,2,3])))

def even1(numbers):
    result=[]
    for number in numbers:
        if number%2==0:
            result.append(number)
    return result

print(even1([1,2,3,4,5]))

def even2(numbers):
    if numbers%2==0:
        return numbers

print(list(map(even2,[1,2,3,4,5,6,7,8,9])))

print(list(map(lambda even: even%2==0,[1,2,3,4,5,6,7,8,9])))
        
# filter(list(map(lambda even: even%2==0,[1,2,3,4,5,6,7,8,9])))
number=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda even3:even3%2==0, number)))
